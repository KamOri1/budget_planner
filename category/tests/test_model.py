"""
Tests for model.
"""

from django.test import TestCase

from users.factories import RandomUserFactory

from ..models import Category, CategoryType


class TestModels(TestCase):
    """Test category model."""

    def setUp(self):
        """Set up test data."""
        self.user = RandomUserFactory()
        self.categoryType = CategoryType.objects.create(type="profit")

    def test_model_Category(self):
        """Test create category"""
        category = CategoryType(
            user_id=self.user, category_type=self.categoryType, category_name="Salary"
        )

        self.assertEqual(str(category.user_id), self.user.username)
        self.assertEqual(str(category), "Salary")
        self.assertEqual(str(category.category_type), self.categoryType.type)
        self.assertTrue(isinstance(category, Category))
