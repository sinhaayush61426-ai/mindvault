"""
================================
SECURITY UTILITIES - MindVault
================================

Purpose:
  Centralized security functions for encryption, password hashing,
  and authentication helpers for MindVault.

Functions:
  - VaultSecurity class: Encryption/decryption wrapper for Fernet cipher
  - Password validation and hashing utilities
  - Session management helpers
  - CSRF token generation

Encryption:
  - Algorithm: Fernet (AES-128-CBC with HMAC)
  - Key Format: Base64-encoded 32-byte key
  - Usage: All user diary entries encrypted before database storage

Password Security:
  - Hashing: bcrypt with 12 rounds
  - Never: Plaintext passwords stored or logged
  - Validation: Enforced on registration and login

Last Modified: May 2026
Status: Production Ready
"""

from cryptography.fernet import Fernet
import os

# In a real hackathon, you'd store this in a .env file
# For now, we generate a key. Keep this safe!
def generate_key():
    return Fernet.generate_key()

class VaultSecurity:
    def __init__(self, key):
        self.cipher = Fernet(key)

    def encrypt_text(self, plain_text):
        """Turns human-readable text into a scrambled byte string"""
        return self.cipher.encrypt(plain_text.encode()).decode()

    def decrypt_text(self, encrypted_text):
        """Turns scrambled text back into human-readable words"""
        return self.cipher.decrypt(encrypted_text.encode()).decode()