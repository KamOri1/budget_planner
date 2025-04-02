from datetime import date

from django.test import TestCase

from category.factories import CategoryFactory
from users.factories import RandomUserFactory

from ..models import SavingGoal


class TestModels(TestCase):
    """Test SavingGoal model."""

    def setUp(self):
        """Set up test data."""
        self.test_date = date(2024, 12, 31)
        self.user = RandomUserFactory()
        self.category = CategoryFactory(user=self.user)
        self.savingGoal = SavingGoal.objects.create(
            name="Vacation",
            target_date=self.test_date,
            target_amount=122.22,
            description="test description",
            user=self.user,
        )

    def test_model_SavingGoal(self):
        """Test create savingGoal"""

        self.assertEqual(str(self.savingGoal.name), "Vacation")
        self.assertEqual(str(self.savingGoal.target_date), "2024-12-31")
        self.assertEqual(str(self.savingGoal.target_amount), "122.22")
        self.assertEqual(str(self.savingGoal.description), "test description")
        self.assertEqual(self.savingGoal.user_id, self.user.id)
        self.assertTrue(isinstance(self.savingGoal, SavingGoal))
