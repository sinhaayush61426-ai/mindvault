# MindVault Quality and Operations Checklist

This document describes the current Django application and provides repeatable checks. It is an operations guide, not a claim of independent security certification.

## Application structure

- `manage.py` starts Django management commands.
- `mindvault/` contains project settings, root URL configuration, and WSGI setup.
- `vault/` contains models, authentication, forms, views, tests, and schema migrations.
- `templates/` contains the Django-rendered pages and generic error pages.
- `static/` contains the responsive blue-and-pink theme, browser scripts, and PWA assets.
- `security.py` encrypts entry text with Fernet before database storage.

## Privacy and account data

- Entry and snapshot content is encrypted before it is stored. The server decrypts content for authenticated views; this is not client-side or zero-knowledge encryption.
- Keep the original `ENCRYPTION_KEY` for existing data. Losing or replacing it makes encrypted content unreadable.
- Passwords are stored as hashes. Bcrypt hashes from earlier installations are upgraded after successful authentication.
- Private queries must be scoped to `request.user`; do not log passwords, keys, plaintext entries, or review form contents.
- Use Django CSRF protection for forms that change data and require authentication for private operations.

## Safe database updates

Back up `instance/mindvault.db` before schema changes. Test adoption of existing data on a separate copy before running migrations on the working vault. Preserve the encryption key and verify account access and content decryption after migration. See [MIGRATION.md](./MIGRATION.md) for the adoption and recovery procedure.

## Local verification

Configure `.env` before running Django commands:

```bash
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py test
```

The test suite should cover authentication, ownership boundaries, encryption, snapshots, CSRF, PWA assets, and expected error responses. Run the tests with a temporary database when validating schema changes.

## Error handling and deployment

- User input is validated in forms and views; validation failures should explain what the user can correct.
- Unexpected failures should be logged without including private content or credentials.
- Decryption failures must not overwrite ciphertext and must be clearly distinguished from valid content.
- Generic `400`, `403`, `404`, and `500` pages avoid exposing debug details. Keep `DEBUG=False` in production.
- Configure a unique `SECRET_KEY`, the correct `ENCRYPTION_KEY`, `ALLOWED_HOSTS`, and secure session/CSRF cookies behind HTTPS.
- Run `python manage.py collectstatic` and serve collected static files from the production web server. Do not use Django's development server in production.
