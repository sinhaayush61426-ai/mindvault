from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import vault.models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("password", models.CharField(db_column="password_hash", max_length=255)),
                ("username", models.CharField(max_length=50, unique=True)),
                ("email", models.EmailField(max_length=120, unique=True)),
                ("created_at", models.DateTimeField(blank=True, null=True)),
            ],
            options={"db_table": "user"},
            managers=[("objects", vault.models.UserManager())],
        ),
        migrations.CreateModel(
            name="DiaryEntry",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("encrypted_content", models.TextField()),
                ("detected_emotion", models.CharField(blank=True, max_length=20, null=True)),
                ("timestamp", models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        db_column="user_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="entries",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"db_table": "diary_entry", "ordering": ["-timestamp"]},
        ),
        migrations.CreateModel(
            name="Review",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("author_name", models.CharField(max_length=50)),
                ("occupation", models.CharField(blank=True, max_length=50, null=True)),
                ("content", models.TextField()),
                ("is_approved", models.BooleanField(default=True)),
                ("timestamp", models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
            options={"db_table": "review", "ordering": ["-timestamp"]},
        ),
        migrations.CreateModel(
            name="Character",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("archetype", models.CharField(blank=True, default="Protagonist", max_length=50, null=True)),
                ("personality_traits", models.TextField(blank=True, null=True)),
                ("backstory", models.TextField(blank=True, null=True)),
                ("relationships", models.TextField(blank=True, null=True)),
                ("physical_description", models.TextField(blank=True, null=True)),
                ("motivations", models.TextField(blank=True, null=True)),
                ("avatar_color", models.CharField(blank=True, default="#5DADE2", max_length=7, null=True)),
                ("created_at", models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ("updated_at", models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        db_column="user_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="characters",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"db_table": "character"},
        ),
        migrations.CreateModel(
            name="EntrySnapshot",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("version", models.CharField(blank=True, default="1.0", max_length=50, null=True)),
                ("encrypted_content", models.BinaryField()),
                ("timestamp", models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ("description", models.CharField(blank=True, max_length=255, null=True)),
                ("is_autosave", models.BooleanField(blank=True, default=False, null=True)),
                (
                    "entry",
                    models.ForeignKey(
                        db_column="entry_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="snapshots",
                        to="vault.diaryentry",
                    ),
                ),
            ],
            options={"db_table": "entry_snapshot", "ordering": ["-timestamp"]},
        ),
        migrations.CreateModel(
            name="FutureLetter",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("encrypted_letter_content", models.TextField()),
                ("unlock_date", models.DateTimeField()),
                ("created_at", models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        db_column="user_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="future_letters",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"db_table": "future_letter"},
        ),
    ]
