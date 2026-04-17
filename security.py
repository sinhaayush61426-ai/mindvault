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