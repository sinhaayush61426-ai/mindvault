from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("An email address is required.")
        if not username:
            raise ValueError("A username is required.")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    password = models.CharField(max_length=255, db_column="password_hash")
    last_login = None

    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=120, unique=True)
    created_at = models.DateTimeField(null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    @property
    def is_active(self):
        return True

    @property
    def is_staff(self):
        return False

    class Meta:
        db_table = "user"

    def __str__(self):
        return self.username


class DiaryEntry(models.Model):
    title = models.CharField(max_length=100, default="New Reflection")
    category = models.CharField(max_length=50, default="General")
    encrypted_content = models.TextField()
    detected_emotion = models.CharField(max_length=20, null=True, blank=True)
    timestamp = models.DateTimeField(default=timezone.now, null=True, blank=True)
    release_date = models.DateTimeField(null=True, blank=True)
    is_time_locked = models.BooleanField(default=False)
    is_draft = models.BooleanField(default=False)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_column="user_id",
        related_name="entries",
    )

    class Meta:
        db_table = "diary_entry"
        ordering = ["-timestamp"]


class Review(models.Model):
    author_name = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50, null=True, blank=True)
    content = models.TextField()
    is_approved = models.BooleanField(default=True)
    timestamp = models.DateTimeField(default=timezone.now, null=True, blank=True)

    class Meta:
        db_table = "review"
        ordering = ["-timestamp"]


class Character(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_column="user_id",
        related_name="characters",
    )
    name = models.CharField(max_length=100)
    archetype = models.CharField(
        max_length=50,
        default="Protagonist",
        null=True,
        blank=True,
    )
    personality_traits = models.TextField(null=True, blank=True)
    backstory = models.TextField(null=True, blank=True)
    relationships = models.TextField(null=True, blank=True)
    physical_description = models.TextField(null=True, blank=True)
    motivations = models.TextField(null=True, blank=True)
    avatar_color = models.CharField(
        max_length=7,
        default="#5DADE2",
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(default=timezone.now, null=True, blank=True)
    updated_at = models.DateTimeField(default=timezone.now, null=True, blank=True)

    class Meta:
        db_table = "character"


class EntrySnapshot(models.Model):
    entry = models.ForeignKey(
        DiaryEntry,
        on_delete=models.CASCADE,
        db_column="entry_id",
        related_name="snapshots",
    )
    version = models.CharField(max_length=50, default="1.0", null=True, blank=True)
    encrypted_content = models.BinaryField()
    timestamp = models.DateTimeField(default=timezone.now, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    is_autosave = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        db_table = "entry_snapshot"
        ordering = ["-timestamp"]


class FutureLetter(models.Model):
    encrypted_letter_content = models.TextField()
    unlock_date = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now, null=True, blank=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_column="user_id",
        related_name="future_letters",
    )

    class Meta:
        db_table = "future_letter"
