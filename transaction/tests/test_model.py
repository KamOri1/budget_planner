"""
Tests for model.
"""

from datetime import datetime, timezone

from django.contrib.auth.models import User
from django.test import TestCase

from category.models import Category, CategoryType

from ..models import Transaction


class TestModels(TestCase):
    """Test transaction model."""

    def setUp(self):
        """Set up test data."""

        self.user = User.objects.create_user(
            username="Test", password="password", email="test@gmail.com"
        )
        self.categoryType = CategoryType.objects.create(type="1")
        self.category = Category.objects.create(
            user=self.user,
            name="Salary",
            type=self.categoryType,
        )
        self.transaction_date_value = datetime(
            2025, 2, 10, 11, 35, 10, tzinfo=timezone.utc
        )

    def test_model_Transaction(self):
        """Test create Transaction"""

        transaction = Transaction.objects.create(
            user=self.user,
            category=self.category,
            sum_amount=433.33,
            description="something to test",
            transaction_name="Shopping",
            transaction_date=self.transaction_date_value,
        )
        self.assertEqual(str(transaction.user), self.user.username)
        self.assertIsNotNone(transaction.create_at)
        self.assertEqual(transaction.transaction_date, self.transaction_date_value)
        self.assertEqual(str(transaction), "Shopping")
        self.assertEqual(str(transaction.description), "something to test")
        self.assertTrue(isinstance(transaction, Transaction))
