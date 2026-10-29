import os
import re
from unittest.mock import patch

import bcrypt
from cryptography.fernet import Fernet
from django.test import RequestFactory, TestCase
from django.views.defaults import (
    bad_request,
    page_not_found,
    permission_denied,
    server_error,
)

from security import VaultSecurity
from .forms import CharacterForm
from .models import Character, DiaryEntry, EntrySnapshot, User


class VaultFlowTests(TestCase):
    def setUp(self):
        self.encryption_key = Fernet.generate_key().decode("ascii")
        self.encryption_patch = patch.dict(
            os.environ,
            {"ENCRYPTION_KEY": self.encryption_key},
        )
        self.encryption_patch.start()
        self.user = User.objects.create_user(
            email="writer@example.com",
            username="writer",
            password="correct horse battery staple",
        )

    def tearDown(self):
        self.encryption_patch.stop()

    def test_registration_login_and_csrf_form(self):
        client = self.client_class(enforce_csrf_checks=True)
        response = client.get("/register")
        token = re.search(
            r'name="csrfmiddlewaretoken" value="([^"]+)"',
            response.content.decode(),
        ).group(1)
        response = client.post(
            "/register",
            {
                "username": "new-writer",
                "email": "new-writer@example.com",
                "password": "a strong password",
                "csrfmiddlewaretoken": token,
            },
        )
        self.assertRedirects(response, "/login")
        self.assertTrue(User.objects.filter(email="new-writer@example.com").exists())

    def test_legacy_bcrypt_password_upgrades_on_login(self):
        password = "legacy password"
        legacy_hash = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt(),
        ).decode("ascii")
        legacy_user = User.objects.create(
            username="legacy",
            email="legacy@example.com",
            password=legacy_hash,
        )

        response = self.client.post(
            "/login",
            {"email": legacy_user.email, "password": password},
        )

        legacy_user.refresh_from_db()
        self.assertRedirects(response, "/dashboard")
        self.assertTrue(legacy_user.password.startswith("pbkdf2_sha256$"))

    def test_django_password_login_and_post_logout(self):
        response = self.client.post(
            "/login",
            {
                "email": self.user.email,
                "password": "correct horse battery staple",
            },
        )
        self.assertRedirects(response, "/dashboard")
        self.assertEqual(self.client.get("/dashboard").status_code, 200)

        response = self.client.post("/logout")
        self.assertRedirects(response, "/")
        self.assertEqual(self.client.get("/dashboard").status_code, 302)

    def test_entry_content_is_encrypted_and_owner_only(self):
        self.client.force_login(self.user)
        response = self.client.post(
            "/seal-letter",
            {
                "title": "Private",
                "category": "General",
                "content": "vault plaintext",
            },
        )

        entry = DiaryEntry.objects.get(user=self.user)
        self.assertRedirects(response, "/dashboard")
        self.assertNotIn("vault plaintext", entry.encrypted_content)
        self.assertContains(
            self.client.get(f"/entry/{entry.pk}"),
            "vault plaintext",
        )

        other_user = User.objects.create_user(
            email="other@example.com",
            username="other",
            password="another password",
        )
        self.client.force_login(other_user)
        self.assertEqual(self.client.get(f"/entry/{entry.pk}").status_code, 404)

    def test_decryption_failure_is_logged_and_shown_without_overwriting_data(self):
        self.client.force_login(self.user)
        entry = DiaryEntry.objects.create(
            user=self.user,
            title="Unreadable draft",
            encrypted_content="invalid ciphertext",
        )

        with self.assertLogs("vault.views", level="WARNING"):
            response = self.client.get(f"/entry/{entry.pk}")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This entry could not be decrypted.")
        self.assertContains(response, "Your encrypted data has not been changed.")
        entry.refresh_from_db()
        self.assertEqual(entry.encrypted_content, "invalid ciphertext")

    def test_editing_unreadable_entry_does_not_replace_encrypted_data(self):
        self.client.force_login(self.user)
        entry = DiaryEntry.objects.create(
            user=self.user,
            title="Unreadable draft",
            encrypted_content="invalid ciphertext",
        )

        with self.assertLogs("vault.views", level="WARNING"):
            response = self.client.post(
                f"/entry/{entry.pk}/edit",
                {"title": "Changed", "content": ""},
            )

        self.assertRedirects(response, f"/entry/{entry.pk}")
        entry.refresh_from_db()
        self.assertEqual(entry.title, "Unreadable draft")
        self.assertEqual(entry.encrypted_content, "invalid ciphertext")

    def test_autosave_encrypts_new_drafts_and_sealing_reuses_them(self):
        self.client.force_login(self.user)
        response = self.client.post(
            "/autosave",
            {
                "title": "Working draft",
                "category": "Research",
                "content": "private draft text",
            },
        )

        self.assertEqual(response.status_code, 200)
        entry = DiaryEntry.objects.get(user=self.user)
        self.assertEqual(response.json(), {"saved": True, "draft_id": entry.pk})
        self.assertTrue(entry.is_draft)
        self.assertNotIn("private draft text", entry.encrypted_content)
        self.assertEqual(
            VaultSecurity().decrypt_text(entry.encrypted_content),
            "private draft text",
        )

        response = self.client.post(
            "/seal-letter",
            {
                "draft_id": str(entry.pk),
                "title": "Finished entry",
                "category": "Fiction",
                "content": "final private text",
            },
        )

        self.assertRedirects(response, "/dashboard")
        self.assertEqual(DiaryEntry.objects.filter(user=self.user).count(), 1)
        entry.refresh_from_db()
        self.assertFalse(entry.is_draft)
        self.assertEqual(entry.title, "Finished entry")
        self.assertEqual(
            VaultSecurity().decrypt_text(entry.encrypted_content),
            "final private text",
        )

    def test_autosave_of_saved_entry_creates_encrypted_owned_snapshot(self):
        self.client.force_login(self.user)
        entry = DiaryEntry.objects.create(
            user=self.user,
            title="Saved entry",
            encrypted_content=VaultSecurity().encrypt_text("original text"),
        )

        response = self.client.post(
            "/autosave",
            {
                "entry_id": str(entry.pk),
                "title": entry.title,
                "content": "updated draft text",
            },
        )

        self.assertEqual(response.status_code, 200)
        snapshot = EntrySnapshot.objects.get(entry=entry)
        self.assertTrue(snapshot.is_autosave)
        self.assertEqual(
            VaultSecurity().decrypt_text(snapshot.encrypted_content),
            "updated draft text",
        )
        entry.refresh_from_db()
        self.assertEqual(
            VaultSecurity().decrypt_text(entry.encrypted_content),
            "original text",
        )

        other_user = User.objects.create_user(
            email="other@example.com",
            username="other",
            password="another password",
        )
        self.client.force_login(other_user)
        self.assertEqual(
            self.client.post(
                "/autosave",
                {"entry_id": str(entry.pk), "content": "cross-account"},
            ).status_code,
            404,
        )
        self.assertEqual(EntrySnapshot.objects.filter(entry=entry).count(), 1)

    def test_autosave_rejects_oversized_input(self):
        self.client.force_login(self.user)

        response = self.client.post(
            "/autosave",
            {"title": "Too large", "content": "x" * 1_000_001},
        )

        self.assertEqual(response.status_code, 400)
        self.assertFalse(DiaryEntry.objects.filter(user=self.user).exists())

    def test_autosave_requires_csrf_protection(self):
        client = self.client_class(enforce_csrf_checks=True)
        client.force_login(self.user)

        response = client.post(
            "/autosave",
            {"title": "Protected draft", "content": "private text"},
        )

        self.assertEqual(response.status_code, 403)
        self.assertFalse(DiaryEntry.objects.filter(user=self.user).exists())

    def test_character_color_rejects_non_hex_css_values(self):
        form = CharacterForm(
            {
                "name": "Aster",
                "avatar_color": "red; background-image: url(//invalid)",
            }
        )

        self.assertFalse(form.is_valid())
        self.assertIn("avatar_color", form.errors)

    def test_authenticated_templates_and_snapshot_restore(self):
        self.client.force_login(self.user)
        entry = DiaryEntry.objects.create(
            user=self.user,
            title="A draft",
            encrypted_content=VaultSecurity().encrypt_text("draft content"),
        )

        for path in (
            "/dashboard",
            "/characters",
            "/character/new",
            f"/entry/{entry.pk}",
            f"/entry/{entry.pk}/edit",
            f"/entry/{entry.pk}/snapshots",
        ):
            with self.subTest(path=path):
                self.assertEqual(self.client.get(path).status_code, 200)

        snapshot_response = self.client.post(
            f"/entry/{entry.pk}/snapshot",
            {"version": "1.1", "description": "Saved draft"},
        )
        self.assertRedirects(snapshot_response, f"/entry/{entry.pk}")
        snapshot = EntrySnapshot.objects.get(entry=entry)

        entry.encrypted_content = VaultSecurity().encrypt_text("new content")
        entry.save(update_fields=["encrypted_content"])
        restore_response = self.client.post(
            f"/snapshot/{snapshot.pk}/restore"
        )
        entry.refresh_from_db()
        self.assertRedirects(restore_response, f"/entry/{entry.pk}")
        self.assertEqual(
            VaultSecurity().decrypt_text(entry.encrypted_content),
            "draft content",
        )

    def test_character_timestamps_are_managed_by_the_server(self):
        self.client.force_login(self.user)
        response = self.client.post(
            "/character/new",
            {"name": "Aster", "archetype": "Mentor", "avatar_color": "#5DADE2"},
        )
        self.assertRedirects(response, "/characters")

        character = Character.objects.get(name="Aster")
        self.assertIsNotNone(character.created_at)
        original_created_at = character.created_at

        response = self.client.post(
            f"/character/{character.pk}/edit",
            {"name": "Aster Vale", "archetype": "Mentor", "avatar_color": "#5DADE2"},
        )
        character.refresh_from_db()
        self.assertRedirects(response, "/characters")
        self.assertEqual(character.created_at, original_created_at)
        self.assertIsNotNone(character.updated_at)

    def test_public_pages_and_manifest_render(self):
        self.assertEqual(self.client.get("/").status_code, 200)
        offline = self.client.get("/offline.html")
        self.assertEqual(offline.status_code, 200)
        self.assertContains(offline, "new changes are not saved while you're offline")
        self.assertEqual(self.client.get("/manifest.json").status_code, 200)
        service_worker = self.client.get("/service-worker.js")
        self.assertEqual(service_worker.status_code, 200)
        self.assertEqual(service_worker["Service-Worker-Allowed"], "/")

    def test_pwa_assets_and_error_pages_work_with_debug_disabled(self):
        with self.settings(DEBUG=False):
            manifest = self.client.get("/manifest.json")
            service_worker = self.client.get("/service-worker.js")
            not_found = self.client.get("/missing-page")

        self.assertEqual(manifest.status_code, 200)
        self.assertEqual(manifest["Content-Type"], "application/manifest+json")
        self.assertEqual(service_worker.status_code, 200)
        self.assertEqual(service_worker["Service-Worker-Allowed"], "/")
        self.assertEqual(service_worker["Cache-Control"], "no-cache")
        self.assertEqual(not_found.status_code, 404)
        self.assertContains(not_found, "We couldn't find that page.", status_code=404)

    def test_generic_error_templates_do_not_expose_debug_details(self):
        request = RequestFactory().get("/")
        with self.settings(DEBUG=False):
            responses = (
                bad_request(request, Exception("internal detail")),
                permission_denied(request, Exception("internal detail")),
                page_not_found(request, Exception("internal detail")),
                server_error(request),
            )

        for response, status, message in zip(
            responses,
            (400, 403, 404, 500),
            (
                "We couldn't process that request.",
                "You don't have permission to view this page.",
                "We couldn't find that page.",
                "Something went wrong.",
            ),
        ):
            with self.subTest(status=status):
                self.assertEqual(response.status_code, status)
                self.assertContains(
                    response,
                    message,
                    status_code=status,
                )
                self.assertNotContains(
                    response,
                    "internal detail",
                    status_code=status,
                )
