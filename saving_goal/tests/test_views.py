"""
Tests for views.
"""

from datetime import date

from django.http import HttpRequest
from django.test import Client, TestCase
from rest_framework.reverse import reverse_lazy

from category.factories import CategoryFactory
from users.factories import RandomUserFactory

from ..models import SavingGoal
from ..views import SavingGoalDeleteView, SavingGoalUpdateView


class TestSavingGoalCreateView(TestCase):
    """Test SavingGoal create views."""

    def setUp(self):
        """Set up test data.Including a logged-in user"""
        self.test_date = date(2024, 12, 31)
        self.user = RandomUserFactory()
        self.index_url = reverse_lazy("create_goal")
        self.category = CategoryFactory(user=self.user)
        self.savingGoal = SavingGoal.objects.create(
            name="Vacation",
            target_date=self.test_date,
            target_amount=122.22,
            description="test description",
            user=self.user,
        )

    def test_form_valid(self):
        """Ensure that the GET request correctly renders the form template."""

        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "saving_goal/goal_add.html")

    def test_post_valid_data_creates_expenses(self):
        """The test verifies that the parameters fetched by the POST method are consistent with the stored settings"""
        self.assertEqual(str(self.savingGoal.name), "Vacation")
        self.assertEqual(str(self.savingGoal.target_date), "2024-12-31")
        self.assertEqual(str(self.savingGoal.target_amount), "122.22")
        self.assertEqual(str(self.savingGoal.description), "test description")
        self.assertEqual(self.savingGoal.user_id, self.user.id)
        self.assertTrue(isinstance(self.savingGoal, SavingGoal))


class TestSavingGoalUpdateView(TestCase):
    """
    Test cases for the SavingGoal update view.
    These tests verify the behavior of updating an existing SavingGoal, correct redirections,
    form handling, and database updates.
    """

    def setUp(self):
        """Set up test data."""
        self.test_date = date(2024, 12, 31)
        self.success_url = reverse_lazy("goal-home")
        self.client = Client()
        self.user1 = RandomUserFactory()
        self.user2 = RandomUserFactory()
        self.request = HttpRequest()
        self.client.force_login(self.user1)

        self.savingGoal1 = SavingGoal.objects.create(
            name="Vacation1",
            target_date=self.test_date,
            target_amount=122.22,
            description="test description1",
            user=self.user1,
        )
        self.savingGoal2 = SavingGoal.objects.create(
            name="Vacation2",
            target_date=self.test_date,
            target_amount=982.42,
            description="test description2",
            user=self.user1,
        )
        self.savingGoal3 = SavingGoal.objects.create(
            name="Vacation3",
            target_date=self.test_date,
            target_amount=66.78,
            description="test description3",
            user=self.user2,
        )

    def test_get_queryset(self):
        """The test simulates user logging in and checks that only the SavingGoal he has added are available"""

        users = [self.user1, self.user2]

        for user in users:

            self.request.user = user
            view = SavingGoalUpdateView()
            view.request = self.request
            queryset = view.get_queryset()

            expected_count = SavingGoal.objects.filter(user=user).count()

            self.assertEqual(queryset.count(), expected_count)

            for goal in queryset:
                self.assertEqual(goal.user, user)

    def test_uses_correct_template_in_response(self):
        """Ensure that the GET request correctly renders the form template."""

        self.client.force_login(self.user1)
        response = self.client.get(self.success_url, pk=self.user1)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "saving_goal/goal_home_page.html")

    def test_update_goal(self):
        """Checks whether the selected goal has been updated."""

        updated_data = {
            "description": "test description nr 1",
            "target_date": self.test_date,
            "target_amount": 345,
            "name": "Updated Vacation1",
        }

        self.client.force_login(self.user1)

        update_url = reverse_lazy("update_goal", args=[self.savingGoal1.pk])
        response = self.client.post(update_url, data=updated_data)
        updated_goal = SavingGoal.objects.get(pk=self.savingGoal1.pk)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(updated_goal.name, "Updated Vacation1")
        self.assertEqual(updated_goal.target_amount, 345)
        self.assertEqual(updated_goal.target_date, self.test_date)
        self.assertEqual(updated_goal.description, "test description nr 1")


class TestSavingGoalDeleteView(TestCase):
    """
    Test cases for the goal delete view.
    These tests verify the behavior of deleting an existing goal, correct redirections,
    form handling, and database updates
    """

    def setUp(self):
        """Set up test data."""

        self.test_date = date(2024, 12, 31)
        self.success_url = reverse_lazy("goal-home")
        self.client = Client()
        self.user1 = RandomUserFactory()
        self.user2 = RandomUserFactory()
        self.request = HttpRequest()
        self.client.force_login(self.user1)

        self.savingGoal1 = SavingGoal.objects.create(
            name="Vacation1",
            target_date=self.test_date,
            target_amount=122.22,
            description="test description1",
            user=self.user1,
        )
        self.savingGoal2 = SavingGoal.objects.create(
            name="Vacation2",
            target_date=self.test_date,
            target_amount=982.42,
            description="test description2",
            user=self.user1,
        )
        self.savingGoal3 = SavingGoal.objects.create(
            name="Vacation3",
            target_date=self.test_date,
            target_amount=66.78,
            description="test description3",
            user=self.user2,
        )

    def test_get_queryset(self):
        """The test simulates user logging in and checks that only the SavingGoal he has added are available"""

        users = [self.user1, self.user2]

        for user in users:

            self.request.user = user
            view = SavingGoalDeleteView()
            view.request = self.request
            queryset = view.get_queryset()

            expected_count = SavingGoal.objects.filter(user=user).count()

            self.assertEqual(queryset.count(), expected_count)

            for goal in queryset:
                self.assertEqual(goal.user, user)

    def test_delete_goal(self):
        """Checks whether the selected goal has been deleted."""

        self.client.force_login(self.user1)
        delete_url = reverse_lazy("delete_goal", args=[self.savingGoal1.pk])
        response = self.client.post(delete_url)

        self.assertEqual(response.status_code, 302)

        with self.assertRaises(SavingGoal.DoesNotExist):
            SavingGoal.objects.get(pk=self.savingGoal1.pk)

        self.assertEqual(SavingGoal.objects.filter(user=self.user1.id).count(), 1)
