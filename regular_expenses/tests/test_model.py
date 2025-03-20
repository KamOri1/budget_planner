from django.test import TestCase

from category.factories import CategoryFactory
from users.factories import RandomUserFactory

from ..models import RegularExpenses


class TestModels(TestCase):
    """Test RegularExpenses model."""

    def setUp(self):
        self.user = RandomUserFactory()
        self.category = CategoryFactory(user=self.user)
        """Set up test data."""
        self.regularExpenses = RegularExpenses.objects.create(
            name="Salary",
            category=self.category,
            sum_amount=122.22,
            description="test description",
            user=self.user,
        )

    def test_model_Category(self):
        """Test create notification"""

        self.assertEqual(str(self.regularExpenses.name), "Salary")
        self.assertEqual(str(self.regularExpenses.category), self.category.name)
        self.assertEqual(str(self.regularExpenses.sum_amount), "122.22")
        self.assertEqual(str(self.regularExpenses.description), "test description")
        self.assertEqual(self.regularExpenses.user_id, self.user.id)
        self.assertTrue(isinstance(self.regularExpenses, RegularExpenses))
