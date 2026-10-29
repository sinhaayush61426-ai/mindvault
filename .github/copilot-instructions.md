---
name: mindvault-workspace-instructions
description: "MindVault Django architecture, encryption, authentication, database, and PWA conventions."
---

# MindVault Workspace Instructions

MindVault is a Django application for a local creative workspace. Preserve the existing feature set and SQLite data when making changes.

## Project structure

- `manage.py`: Django command-line entry point
- `mindvault/`: project settings, root URL configuration, and WSGI application
- `vault/`: models, forms, views, authentication backend, tests, and migrations
- `templates/`: Django templates
- `static/`: CSS, JavaScript, and PWA assets
- `security.py`: Fernet encryption utilities

Run locally with:

```bash
python manage.py migrate
python manage.py runserver
```

For a pre-existing SQLite database, first make a backup and run `python manage.py migrate --fake-initial`. The default database path is `instance/mindvault.db`.

## Django conventions

- Put route handlers in `vault/views.py`, route names in `mindvault/urls.py`, and database models in `vault/models.py`.
- Use Django ORM queries and `get_object_or_404`; filter user-owned data by `request.user` in the query.
- Protect private views with `@login_required` and mutations with the appropriate HTTP-method decorator.
- Use Django forms for validation, Django messages for user feedback, and `{% csrf_token %}` in every POST form.
- Use `{% url %}` and `{% static %}` template tags rather than hard-coded application URLs.
- Add and commit Django schema migrations for model changes. Preserve existing table names and legacy fields unless a reviewed migration explicitly changes them.

## Encryption and account compatibility

- Never store entry or snapshot plaintext. Encrypt entry content with `VaultSecurity` before saving.
- Automatic editor saves must post to the authenticated `/autosave` view so the server encrypts content before writing it to SQLite. Never persist entry text to browser storage.
- Keep the existing `ENCRYPTION_KEY` stable when working with an existing database; rotating it requires a planned data re-encryption.
- The authentication backend accepts bcrypt password hashes from earlier installations and upgrades them to Django password hashes after a valid login. New passwords must use Django's `set_password`.
- Never log passwords, encryption keys, or decrypted content.

## Frontend and PWA

- Keep the existing vanilla JavaScript, Django templates, and CSS variable patterns.
- Test static paths, the manifest, and root-scoped service worker after changing PWA assets or routes.
- Treat offline/browser storage as local data; do not claim server-side encryption is client-side or zero-knowledge.

## Validation

Run focused tests first, then the project checks:

```bash
python manage.py test
python manage.py check
python manage.py makemigrations --check --dry-run
```
