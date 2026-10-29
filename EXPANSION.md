# MindVault Feature Guide

MindVault is a Django application for private writing and creative work. Its pages use Django templates, and its browser assets are kept in `static/`.

## Entries and time locks

Create an entry from the dashboard, choose a category, and write its content. Entry text is encrypted with the configured Fernet key before it is stored. Titles, categories, time-lock metadata, and character profiles are ordinary database fields.

An optional future release date prevents the entry from being viewed or edited until that date. Keep the same `ENCRYPTION_KEY` used by the existing database; without it, encrypted content cannot be recovered.

## Automatic saves and snapshots

- On the dashboard, automatic saves create an encrypted, unsealed draft. Submitting the entry seals that same draft rather than creating a duplicate.
- While editing a saved entry, automatic saves create encrypted snapshots. They do not replace the live entry until the user submits the edit form.
- Automatic saves run on a timer and when the editor loses focus. They require a server connection; the app does not queue entry changes offline.
- Manual snapshots can be labeled with a version and description from an entry's view page.
- Restoring a snapshot replaces the entry's current encrypted content. The snapshot itself remains in history.

Existing browser drafts from earlier builds are not imported automatically. Check the browser that was used for earlier writing before clearing its site data.

## Character profiles

The Character Matrix supports creating, editing, and deleting profiles for the signed-in user. Profiles include a name, archetype, personality traits, backstory, relationships, physical description, motivations, and a validated hex avatar color. Profile text is not encrypted in the database.

## Zen Mode

Zen Mode hides surrounding navigation and shows live word and character counts while editing. Its on/off preference is stored in browser local storage; entry text is not stored there by the current auto-save code.

## Progressive Web App and offline behavior

MindVault provides a web manifest and a service worker that caches static application assets and an offline fallback page. The fallback explains that new edits are not saved while offline. The service worker does not provide offline entry editing or automatic synchronization.

Installability and available browser features vary by platform. The manifest's shortcuts are convenience links and do not replace normal sign-in and authorization checks.

## Visual system

The shared CSS uses a dark navy base with blue and pink accents, responsive layouts, visible keyboard focus, and shared form, card, status, and error-page styling. Core styles are in `static/css/style.css`; feature-specific components are in `static/css/expansion.css`.

## Main feature routes

| Route | Behavior |
|---|---|
| `/dashboard` | View the current user's entries and create new work |
| `/autosave` | Authenticated, CSRF-protected encrypted automatic save |
| `/entry/<id>` | View an owned, unlocked entry |
| `/entry/<id>/edit` | Edit an owned, unlocked entry |
| `/entry/<id>/snapshot` | Create a manual snapshot |
| `/entry/<id>/snapshots` | View snapshot history |
| `/snapshot/<id>/restore` | Restore an owned snapshot |
| `/characters` | View the current user's character profiles |
| `/character/new` | Create a profile |
| `/character/<id>/edit` | Edit an owned profile |
| `/character/<id>/delete` | Delete an owned profile |

## Development checks

```bash
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py test
```

See [README.md](./README.md) for installation and [MIGRATION.md](./MIGRATION.md) for safe existing-database adoption.
