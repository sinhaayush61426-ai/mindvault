from django.urls import path
from django.views.generic import TemplateView

from vault import views


urlpatterns = [
    path("", views.home, name="home"),
    path("register", views.register, name="register"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("submit-review", views.submit_review, name="submit_review"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("seal-letter", views.seal_letter, name="seal_letter"),
    path("autosave", views.autosave_entry, name="autosave_entry"),
    path("characters", views.characters, name="characters"),
    path("character/new", views.new_character, name="new_character"),
    path(
        "character/<int:character_id>/edit",
        views.edit_character,
        name="edit_character",
    ),
    path(
        "character/<int:character_id>/delete",
        views.delete_character,
        name="delete_character",
    ),
    path(
        "entry/<int:entry_id>/snapshot",
        views.create_snapshot,
        name="create_snapshot",
    ),
    path(
        "entry/<int:entry_id>/snapshots",
        views.view_snapshots,
        name="view_snapshots",
    ),
    path(
        "snapshot/<int:snapshot_id>/restore",
        views.restore_snapshot,
        name="restore_snapshot",
    ),
    path("entry/<int:entry_id>", views.view_entry, name="view_entry"),
    path("entry/<int:entry_id>/edit", views.edit_entry, name="edit_entry"),
    path("offline.html", TemplateView.as_view(template_name="offline.html"), name="offline"),
    path(
        "manifest.json",
        views.manifest,
        name="manifest",
    ),
    path("service-worker.js", views.service_worker, name="service_worker"),
]
