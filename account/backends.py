from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class EmailBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=username)  # Use `username` to hold email
            if user.check_password(password):
                return user
            else:
                print(f"Incorrect password for user: {username}")  # Debug statement
                return None  # Explicitly return None if password is incorrect
        except User.DoesNotExist:
            print(f"User does not exist: {username}")  # Debug statement
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
