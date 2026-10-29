# MindVault Setup

## Requirements

- Python 3.10+
- SQLite 3

## Install

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Set `SECRET_KEY` and `ENCRYPTION_KEY` in `.env`. For an existing vault, use the same `ENCRYPTION_KEY` that encrypted its entries; changing it makes existing content unreadable.

Generate keys with:

```bash
python -c "import secrets; print(secrets.token_urlsafe(50))"
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
```

## Database and startup

The default SQLite file is `instance/mindvault.db`; override it with `DATABASE_PATH`.

For an existing installation, stop the running server, make a backup of the database, then adopt the existing tables and add Django's schema:

```bash
cp instance/mindvault.db instance/mindvault.db.backup
python manage.py migrate --fake-initial
```

The initial migration matches the existing `user`, `diary_entry`, `entry_snapshot`, `character`, `review`, and `future_letter` tables. Follow-up migrations add entry title, category, time-lock, and draft fields. Existing bcrypt password hashes are verified at login and upgraded to Django's password hashing format after successful authentication.

For a fresh install, run:

```bash
python manage.py migrate
```

Then start the development server:

```bash
python manage.py check
python manage.py runserver
```

Open <http://127.0.0.1:8000>.

## Tests

```bash
python manage.py test
```

## Production

Set `DEBUG=False`, a unique high-entropy `SECRET_KEY`, the existing vault's `ENCRYPTION_KEY`, `ALLOWED_HOSTS`, `SESSION_COOKIE_SECURE=True`, and `CSRF_COOKIE_SECURE=True`. Run `python manage.py collectstatic` and serve the collected assets from `staticfiles/`. Serve the Django WSGI application at `mindvault.wsgi:application` behind an HTTPS-terminating production server. Do not use `runserver` in production.
