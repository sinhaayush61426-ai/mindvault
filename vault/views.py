import logging

from cryptography.fernet import InvalidToken
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.db import DatabaseError, IntegrityError, transaction
from django.http import FileResponse, HttpResponseBadRequest, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.http import require_POST
from django.conf import settings

from security import VaultSecurity
from .forms import CharacterForm, RegistrationForm, ReviewForm
from .models import Character, DiaryEntry, EntrySnapshot, Review


logger = logging.getLogger(__name__)


def service_worker(request):
    response = _serve_required_asset(
        settings.BASE_DIR / "static" / "js" / "service-worker.js",
        "application/javascript",
    )
    response["Service-Worker-Allowed"] = "/"
    return response


def manifest(request):
    return _serve_required_asset(
        settings.BASE_DIR / "manifest.json",
        "application/manifest+json",
    )


def _serve_required_asset(path, content_type):
    try:
        asset = path.open("rb")
    except OSError:
        logger.exception("Required application asset is unavailable: %s", path.name)
        raise

    response = FileResponse(asset, content_type=content_type)
    response["Cache-Control"] = "no-cache"
    return response


def _show_form_errors(request, form):
    for errors in form.errors.values():
        for error in errors:
            messages.error(request, error)


def _decrypt_entry(entry):
    try:
        return VaultSecurity().decrypt_text(entry.encrypted_content)
    except (InvalidToken, UnicodeDecodeError, TypeError):
        logger.warning(
            "Unable to decrypt content for entry %s.",
            entry.pk,
            exc_info=True,
        )
        return None


def _entry_for_user(entry_id, user):
    return get_object_or_404(DiaryEntry, pk=entry_id, user=user)


def _snapshot_for_user(snapshot_id, user):
    return get_object_or_404(
        EntrySnapshot.objects.select_related("entry"),
        pk=snapshot_id,
        entry__user=user,
    )


def home(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    reviews = Review.objects.filter(is_approved=True)[:3]
    return render(request, "index.html", {"reviews": reviews})


def register(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    get_user_model().objects.create_user(
                        email=form.cleaned_data["email"],
                        username=form.cleaned_data["username"],
                        password=form.cleaned_data["password"],
                    )
            except IntegrityError:
                messages.error(
                    request,
                    "That username or email is already in use.",
                )
                return redirect("register")
            messages.success(request, "Account created successfully! Please log in.")
            return redirect("login")
        _show_form_errors(request, form)
    return render(request, "register.html")


def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        user = authenticate(
            request,
            email=request.POST.get("email", "").strip(),
            password=request.POST.get("password", ""),
        )
        if user is not None:
            login(request, user)
            next_page = request.POST.get("next") or request.GET.get("next")
            if not next_page or not url_has_allowed_host_and_scheme(
                next_page,
                allowed_hosts={request.get_host()},
                require_https=request.is_secure(),
            ):
                next_page = "dashboard"
            messages.success(request, "Welcome back! Redirecting you to your vault…")
            return redirect(next_page)
        messages.error(request, "Invalid email or password. Please try again.")
        return redirect("login")

    return render(request, "login.html")


@require_POST
def logout_view(request):
    logout(request)
    return redirect("home")


def submit_review(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            Review.objects.create(
                author_name=form.cleaned_data["author_name"],
                occupation=form.cleaned_data["occupation"],
                content=form.cleaned_data["content"],
                is_approved=False,
            )
            messages.success(
                request,
                "Thank you! Your review will be displayed after moderation.",
            )
            return redirect("home")
        _show_form_errors(request, form)
    return render(request, "submit_review.html")


@login_required
def dashboard(request):
    entries = list(
        DiaryEntry.objects.filter(user=request.user).order_by("-timestamp")
    )
    now = timezone.now()
    for entry in entries:
        entry.is_locked = bool(entry.release_date and entry.release_date > now)
    return render(request, "dashboard.html", {"entries": entries})


@login_required
@require_POST
def seal_letter(request):
    content = request.POST.get("content", "")
    title = request.POST.get("title", "").strip()
    draft_id = request.POST.get("draft_id", "").strip()
    if not title or len(title) > 100 or len(content) > 1_000_000:
        messages.error(request, "Enter a title and keep the entry under 1 MB.")
        return redirect("dashboard")

    release_date = None
    release_date_value = request.POST.get("release_date", "").strip()
    if request.POST.get("enable_time_lock") and not release_date_value:
        messages.error(request, "Select a release date for this time-locked entry.")
        return redirect("dashboard")
    if release_date_value:
        release_date = parse_datetime(release_date_value)
        if release_date is None:
            messages.error(request, "Invalid release date format.")
            return redirect("dashboard")
        if timezone.is_naive(release_date):
            release_date = timezone.make_aware(
                release_date,
                timezone.get_current_timezone(),
            )
        if release_date <= timezone.now():
            messages.error(request, "Release date must be in the future.")
            return redirect("dashboard")

    category = request.POST.get("category", "General")[:50] or "General"
    encrypted_content = VaultSecurity().encrypt_text(content)
    if draft_id:
        if not draft_id.isascii() or not draft_id.isdecimal():
            return HttpResponseBadRequest("Invalid draft identifier.")
        entry = get_object_or_404(
            DiaryEntry,
            pk=draft_id,
            user=request.user,
            is_draft=True,
        )
        entry.title = title
        entry.category = category
        entry.encrypted_content = encrypted_content
        entry.release_date = release_date
        entry.is_time_locked = release_date is not None
        entry.is_draft = False
        entry.save(
            update_fields=[
                "title",
                "category",
                "encrypted_content",
                "release_date",
                "is_time_locked",
                "is_draft",
            ]
        )
    else:
        DiaryEntry.objects.create(
            title=title,
            category=category,
            encrypted_content=encrypted_content,
            release_date=release_date,
            is_time_locked=release_date is not None,
            user=request.user,
        )
    messages.success(
        request,
        "Time-locked letter sealed!" if release_date else "Entry sealed!",
    )
    return redirect("dashboard")


@login_required
@require_POST
def autosave_entry(request):
    title = request.POST.get("title", "").strip()
    content = request.POST.get("content", "")
    category = request.POST.get("category", "General").strip() or "General"
    entry_id = request.POST.get("entry_id", "").strip()
    draft_id = request.POST.get("draft_id", "").strip()

    if len(title) > 100 or len(category) > 50 or len(content) > 1_000_000:
        return JsonResponse(
            {"error": "Keep the title under 100 characters and the entry under 1 MB."},
            status=400,
        )
    if not title and not content and not (entry_id or draft_id):
        return JsonResponse({"saved": False}, status=204)
    if entry_id and draft_id:
        return JsonResponse(
            {"error": "Choose either a saved entry or a new draft."},
            status=400,
        )
    if entry_id and (not entry_id.isascii() or not entry_id.isdecimal()):
        return JsonResponse({"error": "Invalid entry identifier."}, status=400)
    if draft_id and (not draft_id.isascii() or not draft_id.isdecimal()):
        return JsonResponse({"error": "Invalid draft identifier."}, status=400)

    encrypted_content = VaultSecurity().encrypt_text(content)
    try:
        with transaction.atomic():
            if entry_id:
                entry = _entry_for_user(entry_id, request.user)
                if entry.release_date and entry.release_date > timezone.now():
                    return JsonResponse(
                        {"error": "This entry is still time-locked."},
                        status=409,
                    )
                EntrySnapshot.objects.create(
                    entry=entry,
                    version="auto",
                    encrypted_content=encrypted_content.encode("ascii"),
                    description="Automatic save",
                    is_autosave=True,
                )
                result = {"saved": True, "entry_id": entry.pk}
            else:
                entry = None
                if draft_id:
                    entry = get_object_or_404(
                        DiaryEntry,
                        pk=draft_id,
                        user=request.user,
                        is_draft=True,
                    )
                if entry is None:
                    entry = DiaryEntry.objects.create(
                        title=title or "New Reflection",
                        category=category,
                        encrypted_content=encrypted_content,
                        is_draft=True,
                        user=request.user,
                    )
                else:
                    entry.title = title or "New Reflection"
                    entry.category = category
                    entry.encrypted_content = encrypted_content
                    entry.save(
                        update_fields=["title", "category", "encrypted_content"]
                    )
                result = {"saved": True, "draft_id": entry.pk}
    except DatabaseError:
        logger.exception(
            "Could not save an encrypted entry for user %s.",
            request.user.pk,
        )
        return JsonResponse(
            {"error": "The draft could not be saved. Please try again."},
            status=503,
        )

    return JsonResponse(result)


@login_required
def characters(request):
    user_characters = Character.objects.filter(user=request.user)
    return render(request, "characters.html", {"characters": user_characters})


@login_required
def new_character(request):
    form = CharacterForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            character = form.save(commit=False)
            character.user = request.user
            character.save()
            messages.success(request, f"Character '{character.name}' created!")
            return redirect("characters")
        _show_form_errors(request, form)
    return render(
        request,
        "character_form.html",
        {"character": None, "form": form},
    )


@login_required
def edit_character(request, character_id):
    character = get_object_or_404(
        Character,
        pk=character_id,
        user=request.user,
    )
    form = CharacterForm(request.POST or None, instance=character)
    if request.method == "POST":
        if form.is_valid():
            character = form.save(commit=False)
            character.updated_at = timezone.now()
            character.save()
            messages.success(request, f"Character '{character.name}' updated!")
            return redirect("characters")
        _show_form_errors(request, form)
    return render(
        request,
        "character_form.html",
        {"character": character, "form": form},
    )


@login_required
@require_POST
def delete_character(request, character_id):
    character = get_object_or_404(
        Character,
        pk=character_id,
        user=request.user,
    )
    character.delete()
    messages.success(request, "Character deleted")
    return redirect("characters")


@login_required
@require_POST
def create_snapshot(request, entry_id):
    entry = _entry_for_user(entry_id, request.user)
    version = request.POST.get("version", "1.0").strip()
    description = request.POST.get("description", "").strip()
    if not version or len(version) > 50 or len(description) > 255:
        return HttpResponseBadRequest("Invalid snapshot version or description.")

    snapshot_content = entry.encrypted_content
    if isinstance(snapshot_content, str):
        snapshot_content = snapshot_content.encode("ascii")
    EntrySnapshot.objects.create(
        entry=entry,
        version=version,
        encrypted_content=snapshot_content,
        description=description,
        is_autosave=False,
    )
    messages.success(request, f"Snapshot '{version}' created!")
    return redirect("view_entry", entry_id=entry_id)


@login_required
def view_snapshots(request, entry_id):
    entry = _entry_for_user(entry_id, request.user)
    snapshots = EntrySnapshot.objects.filter(entry=entry)
    return render(
        request,
        "snapshots.html",
        {"entry": entry, "snapshots": snapshots},
    )


@login_required
@require_POST
def restore_snapshot(request, snapshot_id):
    snapshot = _snapshot_for_user(snapshot_id, request.user)
    snapshot_content = snapshot.encrypted_content
    if isinstance(snapshot_content, bytes):
        snapshot_content = snapshot_content.decode("ascii")
    snapshot.entry.encrypted_content = snapshot_content
    snapshot.entry.save(update_fields=["encrypted_content"])
    messages.success(request, f"Entry restored to version {snapshot.version}")
    return redirect("view_entry", entry_id=snapshot.entry_id)


@login_required
def view_entry(request, entry_id):
    entry = _entry_for_user(entry_id, request.user)
    if entry.release_date and entry.release_date > timezone.now():
        messages.error(request, "This entry is still time-locked.")
        return redirect("dashboard")
    content = _decrypt_entry(entry)
    return render(
        request,
        "view_entry.html",
        {
            "entry": entry,
            "content": content,
            "content_error": content is None,
        },
    )


@login_required
def edit_entry(request, entry_id):
    entry = _entry_for_user(entry_id, request.user)
    if entry.release_date and entry.release_date > timezone.now():
        messages.error(request, "This entry is still time-locked.")
        return redirect("dashboard")

    content = _decrypt_entry(entry)
    if content is None:
        messages.error(
            request,
            "This entry cannot be edited until its encrypted content can be decrypted.",
        )
        return redirect("view_entry", entry_id=entry.id)

    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        content = request.POST.get("content", "")
        if not title or len(title) > 100 or len(content) > 1_000_000:
            messages.error(request, "Enter a title and keep the entry under 1 MB.")
            return redirect("edit_entry", entry_id=entry.id)
        entry.title = title
        entry.category = request.POST.get("category", "General")[:50] or "General"
        entry.encrypted_content = VaultSecurity().encrypt_text(content)
        entry.is_draft = False
        entry.save(
            update_fields=["title", "category", "encrypted_content", "is_draft"]
        )
        messages.success(request, "Entry updated!")
        return redirect("view_entry", entry_id=entry.id)

    return render(
        request,
        "entry.html",
        {"entry": entry, "content": content},
    )
