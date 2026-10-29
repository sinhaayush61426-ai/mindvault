# Existing Database Adoption

MindVault uses Django for request handling, authentication, sessions, templates, database access, and schema migrations. Existing installations can keep using `instance/mindvault.db`.

## Adopt an existing database

1. Stop the application and make a backup before changing the schema:

   ```bash
   cp instance/mindvault.db instance/mindvault.db.backup
   ```

2. Keep the existing `ENCRYPTION_KEY`. A different key cannot decrypt existing entries and snapshots.
3. Configure `SECRET_KEY`, `ENCRYPTION_KEY`, and `DATABASE_PATH` in `.env`, then install the project dependencies.
4. Confirm the database path points to the backed-up vault and that the expected application tables are present.
5. Adopt the initial schema and apply later changes:

   ```bash
   python manage.py migrate --fake-initial
   ```

6. Verify the application and launch it:

   ```bash
   python manage.py check
   python manage.py test
   python manage.py runserver
   ```

The initial migration recognizes the existing `user`, `diary_entry`, `entry_snapshot`, `character`, `review`, and `future_letter` tables. Follow-up migrations add entry title, category, release date, time-lock, and draft fields without replacing encrypted content. Existing bcrypt password hashes remain usable and are upgraded after a successful login.

`--fake-initial` is safe only when all tables in the initial migration already exist with compatible columns. If a table is missing or has a different schema, stop and investigate before applying migrations. Do not delete the database or run a second application version against a database after its schema has changed.

For additional confidence, test adoption on a separate copy of the database first. Keep the backup until you have verified account access, entry counts, and decryption with the original encryption key.

## Fresh installations

```bash
pip install -r requirements.txt
cp .env.example .env
# Configure a strong SECRET_KEY and a valid Fernet ENCRYPTION_KEY.
python manage.py migrate
python manage.py runserver
```

## Recovery

If adoption fails, stop the application and restore the backup made before migration. Keep the original encryption key. Do not attempt to repair a partially changed vault by deleting tables or regenerating the key.

## Routes retained

The existing page URLs remain available: `/`, `/register`, `/login`, `/logout`, `/dashboard`, `/seal-letter`, `/entry/<id>`, `/entry/<id>/edit`, `/entry/<id>/snapshots`, `/entry/<id>/snapshot`, `/snapshot/<id>/restore`, `/characters`, `/character/new`, `/character/<id>/edit`, `/character/<id>/delete`, and `/submit-review`.
