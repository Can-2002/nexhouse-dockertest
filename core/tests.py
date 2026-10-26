from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.db import OperationalError
from django.test import TestCase
from django.urls import reverse


class EnvironmentTests(TestCase):
    def test_home_is_accessible(self):
        self.assertContains(self.client.get(reverse("home")), "Nexhouse")

    def test_health_checks_database(self):
        self.assertEqual(self.client.get(reverse("health")).json(), {"status": "ok"})

    def test_health_hides_database_error_details(self):
        with patch("core.views.connection.cursor", side_effect=OperationalError("secret")):
            response = self.client.get(reverse("health"))
        self.assertEqual(response.status_code, 503)
        self.assertNotContains(response, "secret", status_code=503)

    def test_admin_requires_login(self):
        response = self.client.get(reverse("admin:index"))
        self.assertRedirects(response, "/admin/login/?next=/admin/", fetch_redirect_response=False)

    def test_regular_user_cannot_access_admin(self):
        user = get_user_model().objects.create_user(username="member", password="test-password")
        self.client.force_login(user)
        self.assertEqual(self.client.get(reverse("admin:index")).status_code, 302)

    def test_superuser_can_access_admin(self):
        user = get_user_model().objects.create_superuser(
            username="admin", email="admin@example.invalid", password="test-password"
        )
        self.assertNotEqual(user.password, "test-password")
        self.assertTrue(user.check_password("test-password"))
        self.client.force_login(user)
        self.assertEqual(self.client.get(reverse("admin:index")).status_code, 200)
