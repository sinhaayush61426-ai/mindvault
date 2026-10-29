# Troubleshooting

## Missing Django or cryptography modules

Install the project's dependencies in the active virtual environment:

```bash
python -m pip install -r requirements.txt
```

## Django system check or missing-table errors

Run the migrations:

```bash
python manage.py check
python manage.py migrate
```

For a pre-existing SQLite database, follow [MIGRATION.md](./MIGRATION.md) and use `python manage.py migrate --fake-initial` after making a backup.

## Existing entries cannot be decrypted

Set `ENCRYPTION_KEY` to the exact Fernet key that was used for the existing database. Do not generate a replacement key for a vault that already contains encrypted data.

## Cannot log in to an existing account

Legacy bcrypt hashes are supported and upgraded after a successful login. Confirm the email and password are correct, and ensure the database path points to the original `instance/mindvault.db`.
