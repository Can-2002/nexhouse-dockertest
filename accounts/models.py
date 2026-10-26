from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Project-owned user model, extendable without replacing Django's user table."""
