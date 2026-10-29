import bcrypt
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class LegacyBcryptBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        email = kwargs.get("email", username)
        if email is None or password is None:
            return None

        user_model = get_user_model()
        try:
            user = user_model._default_manager.get_by_natural_key(email)
        except user_model.DoesNotExist:
            user_model().set_password(password)
            return None

        stored_hash = user.password
        if stored_hash.startswith(("$2a$", "$2b$", "$2y$")):
            try:
                valid = bcrypt.checkpw(
                    password.encode("utf-8"),
                    stored_hash.encode("utf-8"),
                )
            except ValueError:
                return None
            if valid:
                user.set_password(password)
                user.save(update_fields=["password"])
        else:
            valid = user.check_password(password)

        if valid and self.user_can_authenticate(user):
            return user
        return None
