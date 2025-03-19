"""
Tests for views.
"""

from django.test import Client, TestCase
from rest_framework.reverse import reverse_lazy

from notifications_type.models import NotificationType
from users.factories import RandomUserFactory

from ..models import Notification


class TestCategoryCreateView(TestCase):
    """Test Notification create views."""

    def setUp(self):
        """Set up test data.Including a logged-in user"""

        self.client = Client()
        self.user = RandomUserFactory()
        self.client.force_login(self.user)
        self.notificationsType = NotificationType.objects.create(
            name="alert",
        )
        self.index_url = reverse_lazy("create_notification")
        self.notification1 = Notification.objects.create(
            user=self.user,
            type=self.notificationsType,
            name="Test1",
            message="Test message",
        )

    def test_form_valid(self):
        """Ensure that the GET request correctly renders the form template."""

        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "notifications/notifications_add.html")

    def test_post_valid_data_creates_category(self):
        self.assertEqual(str(self.notification1.user), self.user.username)
        self.assertEqual(str(self.notification1), "Test1")
        self.assertEqual(str(self.notification1.type), self.notificationsType.name)
        self.assertEqual(str(self.notification1.name), "Test1")
        self.assertEqual(str(self.notification1.message), "Test message")
        self.assertTrue(isinstance(self.notification1, Notification))
