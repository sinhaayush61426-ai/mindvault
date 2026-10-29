# MindVault

MindVault is a private writing workspace for journal entries, research notes, and creative projects. It is built with Django, SQLite, server-side Fernet encryption for entry content, and a responsive dark blue-and-pink interface.

## Features

- Account registration and login, including upgrade of existing bcrypt password hashes after a successful login.
- Encrypted entries with categories and optional time locks.
- Encrypted automatic saves: new work is saved as a draft; edits to existing entries are stored as encrypted snapshots. Automatic saves require a server connection.
- Manual snapshots and restore for entry history.
- Private character profiles and moderated public reviews.
- Zen Mode with a live word/character counter.
- Progressive Web App manifest, cached application assets, and an offline fallback page.

The service worker caches the application shell only. It does not save or sync edits while offline. Entry content is encrypted before database storage, then decrypted by the server for an authenticated view; this is not client-side or zero-knowledge encryption. Character profile fields are not encrypted.

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Set a unique `SECRET_KEY` and a valid Fernet `ENCRYPTION_KEY` in `.env`, then initialize a fresh database and run the app:

```bash
python -c "import secrets; print(secrets.token_urlsafe(50))"
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
python manage.py migrate
python manage.py check
python manage.py runserver
```

Open <http://127.0.0.1:8000>.

## Existing database

The default database is `instance/mindvault.db`. For an existing vault, stop the application and back up the database before applying schema changes:

```bash
cp instance/mindvault.db instance/mindvault.db.backup
```

Keep the original `ENCRYPTION_KEY`. Set `DATABASE_PATH` to the existing database and run:

```bash
python manage.py migrate --fake-initial
python manage.py check
python manage.py test
```

The initial migration adopts the existing application tables. Later migrations add entry fields and the encrypted-draft marker without replacing existing content. Test adoption against a separate database copy first; do not run migration commands against a valuable vault until its backup is verified. See [MIGRATION.md](./MIGRATION.md).

## Architecture

```text
manage.py                 Django command-line entry point
mindvault/                Settings, root URLs, and WSGI application
vault/                    Models, forms, auth backend, views, and migrations
templates/                Server-rendered pages and error pages
static/css/               Blue-and-pink responsive styles
static/js/                Editor behavior and PWA service worker
security.py               Fernet encryption helpers
instance/mindvault.db     Local SQLite database (not committed)
```

### Main routes

| Route | Purpose |
|---|---|
| `/register`, `/login`, `/logout` | Account access |
| `/dashboard`, `/seal-letter`, `/autosave` | View, create, and save entries |
| `/entry/<id>`, `/entry/<id>/edit` | View and edit an entry |
| `/entry/<id>/snapshot`, `/entry/<id>/snapshots` | Create and view snapshots |
| `/snapshot/<id>/restore` | Restore a snapshot |
| `/characters`, `/character/new`, `/character/<id>/edit`, `/character/<id>/delete` | Manage character profiles |
| `/submit-review` | Submit a review for moderation |
| `/manifest.json`, `/service-worker.js`, `/offline.html` | PWA resources |

Private records are scoped to the authenticated user. All data-changing forms use Django CSRF protection.

## Automatic saving and browser data

Automatic saves are submitted to the authenticated Django application and encrypted before being written to SQLite. New work remains an unsealed draft until submitted; automatic saves of existing entries create encrypted snapshots. A connection is required.

Earlier browser builds may have left an unsaved draft in that browser's local storage. The current app does not import it automatically. Check for any work you need before clearing browser site data.

## Checks and tests

Configure `.env`, then run:

```bash
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py test
```

Use a temporary database when verifying migrations. The test suite covers authentication, CSRF, data ownership, encryption, snapshots, automatic saves, PWA resources, and error states.

## Production

Set `DEBUG=False`, a unique `SECRET_KEY`, the correct `ENCRYPTION_KEY`, and `ALLOWED_HOSTS`. Enable secure session and CSRF cookies behind HTTPS. Run `python manage.py collectstatic` and serve collected static files from a production web server; do not use `runserver` in production.

## Documentation

- [Setup guide](./SETUP_GUIDE.md)
- [Database adoption and recovery](./MIGRATION.md)
- [Feature guide](./EXPANSION.md)
- [Quality and operations checklist](./COMPREHENSIVE_AUDIT.md)
- [Troubleshooting](./ERROR_FIX.md)
