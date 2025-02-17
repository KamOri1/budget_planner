"""
Tests for model.
"""

from django.contrib.auth.models import User
from django.test import TestCase

from ..models import Category


class TestModels(TestCase):
    """Test category model."""

    def setUp(self):
        """Set up test data."""

        self.user = User.objects.create_user(
            username="Test", password="password", email="test@gmail.com"
        )

    def test_model_Category(self):
        """Test create category"""

        category = Category.objects.create(
            user_id=self.user,
            category_name="Salary",
            category_type="profit",
        )
        self.assertEqual(str(category.user_id), self.user.username)
        self.assertEqual(str(category), "Salary")
        self.assertEqual(str(category.category_type), "profit")
        self.assertTrue(isinstance(category, Category))
