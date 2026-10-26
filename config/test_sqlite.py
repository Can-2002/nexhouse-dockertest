"""Optional lightweight fallback; authoritative CI tests use PostgreSQL."""

from .settings import *  # noqa: F403

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}}
