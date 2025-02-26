"""
Tests for model.
"""

from django.test import TestCase

from users.factories import RandomUserFactory

from ..factories import RandomCategoryFactory
from ..models import Category, CategoryType


class TestModels(TestCase):
    """Test category model."""

    def setUp(self):
        """Set up test data."""
        self.user = RandomUserFactory()
        # self.user = User.objects.create_user(
        #     username="Test", password="password", email="test@gmail.com"
        # )
        self.categoryType = CategoryType.objects.create(type="profit")

    def test_model_Category(self):
        """Test create category"""
        category = RandomCategoryFactory(
            user_id=self.user, category_type=self.categoryType, category_name="Salary"
        )
        # category = Category.objects.create(
        #     user_id=self.user,
        #     category_name="Salary",
        #     category_type=self.categoryType,
        # )
        self.assertEqual(str(category.user_id), self.user.username)
        self.assertEqual(str(category), "Salary")
        self.assertEqual(str(category.category_type), self.categoryType.type)
        self.assertTrue(isinstance(category, Category))
