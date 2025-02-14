"""
Tests for model.
"""

from datetime import datetime, timezone

from django.contrib.auth.models import User
from django.test import TestCase

from category.models import Category

from ..models import Transaction


class TestModels(TestCase):
    """Test transaction model."""

    def setUp(self):
        """Set up test data."""

        self.user = User.objects.create_user(
            username="Test", password="password", email="test@gmail.com"
        )
        self.category = Category.objects.create(
            user_id=self.user,
            category_name="Salary",
            category_type="profit",
        )
        self.create_at_value = datetime(2025, 2, 12, 10, 30, 0, tzinfo=timezone.utc)
        self.transaction_date_value = datetime(
            2025, 2, 10, 11, 35, 10, tzinfo=timezone.utc
        )

    def test_model_Transaction(self):
        """Test create Transaction"""

        transaction = Transaction.objects.create(
            user_id=self.user,
            category_id=self.category,
            sum_amount=433.33,
            description="something to test",
            transaction_name="Shopping",
            create_at=self.create_at_value,
            transaction_date=self.transaction_date_value,
        )
        self.assertEqual(str(transaction.user_id), self.user.username)
        # self.assertEqual(transaction.create_at, self.create_at_value)
        self.assertEqual(transaction.transaction_date, self.transaction_date_value)
        self.assertEqual(str(transaction), "Shopping")
        self.assertEqual(str(transaction.description), "something to test")
        self.assertTrue(isinstance(transaction, Transaction))
