"""
Tests for views.
"""

from django.http import HttpRequest
from django.test import Client, TestCase
from rest_framework.reverse import reverse_lazy

from notifications_type.models import NotificationType
from users.factories import RandomUserFactory

from ..models import Notification
from ..views import NotificationDeleteView, NotificationUpdateView


class TestNotificationCreateView(TestCase):
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


class TestNotificationUpdateView(TestCase):
    """
    Test cases for the Notification update view.
    These tests verify the behavior of updating an existing Notification, correct redirections,
    form handling, and database updates.
    """

    def setUp(self):
        """Set up test data.Including a logged-in user"""
        self.success_url = reverse_lazy("notification_home")
        self.notificationsType = NotificationType.objects.create(
            name="alert",
        )
        self.client = Client()
        self.user1 = RandomUserFactory()
        self.user2 = RandomUserFactory()
        self.request = HttpRequest()

        self.notification1 = Notification.objects.create(
            user=self.user1,
            type=self.notificationsType,
            name="Test1",
            message="Test message",
        )
        self.notification2 = Notification.objects.create(
            user=self.user1,
            type=self.notificationsType,
            name="Test2",
            message="Test message 2",
        )
        self.notification3 = Notification.objects.create(
            user=self.user2,
            type=self.notificationsType,
            name="Test3",
            message="Test message 3",
        )

    def test_get_queryset(self):
        """The test simulates user logging in and checks that only the Notifications he has added are available"""

        users = [self.user1, self.user2]

        for user in users:

            self.request.user = user
            view = NotificationUpdateView()
            view.request = self.request
            queryset = view.get_queryset()

            expected_count = Notification.objects.filter(user=user).count()

            self.assertEqual(queryset.count(), expected_count)

            for category in queryset:
                self.assertEqual(category.user, user)

    def test_uses_correct_template_in_response(self):
        """Ensure that the GET request correctly renders the form template."""

        self.client.force_login(self.user1)
        response = self.client.get(self.success_url, pk=self.user1)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "notifications/notifications_home_page.html")

    def test_update_notification(self):
        """Checks whether the selected notification has been updated."""

        updated_data = {
            "type": self.notificationsType.pk,
            "name": "Updated test",
            "message": "Updated message",
        }

        self.client.force_login(self.user1)

        update_url = reverse_lazy("update_notification", args=[self.notification1.pk])
        response = self.client.post(update_url, data=updated_data)
        updated_notification = Notification.objects.get(pk=self.notification1.pk)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(updated_notification.name, "Updated test")
        self.assertEqual(updated_notification.type, self.notificationsType)
        self.assertEqual(updated_notification.message, "Updated message")


class TestNotificationDeleteView(TestCase):
    """
    Test cases for the Notification delete view.
    These tests verify the behavior of deleting an existing Notification, correct redirections,
    form handling, and database updates
    """

    def setUp(self):
        """Set up test data."""
        self.success_url = reverse_lazy("notification_home")
        self.notificationsType = NotificationType.objects.create(
            name="alert",
        )
        self.client = Client()
        self.user1 = RandomUserFactory()
        self.user2 = RandomUserFactory()
        self.request = HttpRequest()

        self.notification1 = Notification.objects.create(
            user=self.user1,
            type=self.notificationsType,
            name="Test1",
            message="Test message",
        )
        self.notification2 = Notification.objects.create(
            user=self.user2,
            type=self.notificationsType,
            name="Test2",
            message="Test message 2",
        )

    def test_get_queryset(self):
        """The test simulates user logging in and checks that only the notifications he has added are available"""

        users = [self.user1, self.user2]

        for user in users:

            self.request.user = user
            view = NotificationDeleteView()
            view.request = self.request
            queryset = view.get_queryset()

            expected_count = Notification.objects.filter(user=user).count()

            self.assertEqual(queryset.count(), expected_count)

            for notification in queryset:
                self.assertEqual(notification.user, user)

    def test_delete_Notification(self):
        """Checks whether the selected notification has been deleted."""

        self.client.force_login(self.user1)
        delete_url = reverse_lazy("delete_notification", args=[self.notification1.pk])
        response = self.client.post(delete_url)

        self.assertEqual(response.status_code, 302)

        with self.assertRaises(Notification.DoesNotExist):
            Notification.objects.get(pk=self.notification1.pk)

        self.assertEqual(Notification.objects.filter(user=self.user1.id).count(), 0)
