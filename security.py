"""Fernet encryption helpers for MindVault entry and snapshot content."""

import os

from cryptography.fernet import Fernet
from django.core.exceptions import ImproperlyConfigured


def generate_key():
    return Fernet.generate_key()


class VaultSecurity:
    def __init__(self, key=None):
        configured_key = key or os.environ.get("ENCRYPTION_KEY")
        if not configured_key:
            raise ImproperlyConfigured(
                "Set ENCRYPTION_KEY to the Fernet key for this vault."
            )
        if isinstance(configured_key, str):
            configured_key = configured_key.encode("ascii")
        self.cipher = Fernet(configured_key)

    def encrypt_text(self, plain_text):
        return self.cipher.encrypt(plain_text.encode("utf-8")).decode("ascii")

    def decrypt_text(self, encrypted_text):
        if isinstance(encrypted_text, str):
            encrypted_text = encrypted_text.encode("ascii")
        return self.cipher.decrypt(encrypted_text).decode("utf-8")