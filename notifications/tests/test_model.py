from django.test import TestCase

from notifications_type.models import NotificationType
from users.factories import RandomUserFactory

from ..models import Notification


class TestModels(TestCase):
    """Test notification model."""

    def setUp(self):
        """Set up test data."""
        self.user = RandomUserFactory()
        self.notificationsType = NotificationType.objects.create(name="alert")

    def test_model_Category(self):
        """Test create notification"""
        notification = Notification(
            user=self.user,
            type=self.notificationsType,
            name="Test1",
            message="Test message",
        )

        self.assertEqual(str(notification.user), self.user.username)
        self.assertEqual(str(notification), "Test1")
        self.assertEqual(str(notification.type), self.notificationsType.name)
        self.assertEqual(str(notification.name), "Test1")
        self.assertEqual(str(notification.message), "Test message")
        self.assertTrue(isinstance(notification, Notification))
