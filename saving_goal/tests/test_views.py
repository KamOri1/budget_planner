"""
Tests for views.
"""

from datetime import date

from django.test import TestCase
from rest_framework.reverse import reverse_lazy

from category.factories import CategoryFactory
from users.factories import RandomUserFactory

from ..models import SavingGoal


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
