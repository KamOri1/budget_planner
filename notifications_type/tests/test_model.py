from django.test import TestCase

from ..models import NotificationType


class TestModels(TestCase):
    """Test notification model."""

    def setUp(self):
        """Set up test data."""
        self.notificationsType = NotificationType.objects.create(name="alert")

    def test_model_Category(self):
        """Test create notification"""

        self.assertEqual(str(self.notificationsType.name), "alert")
        self.assertTrue(isinstance(self.notificationsType, NotificationType))
