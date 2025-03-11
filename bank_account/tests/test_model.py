"""
Tests for model.
"""

from django.test import TestCase

from users.factories import RandomUserFactory

from ..models import BankAccount


class TestModels(TestCase):
    """Test BankAccount model."""

    def setUp(self):
        """Set up test data."""
        self.user = RandomUserFactory()

    def test_model_BankAccount(self):
        """Test create BankAccount"""
        bank_account = BankAccount(
            user=self.user, name="PKO", number="12345", sum_of_funds=12000
        )

        self.assertEqual(str(bank_account.user), self.user.username)
        self.assertEqual(str(bank_account.name), "PKO")
        self.assertEqual(str(bank_account.number), "12345")
        self.assertEqual(str(bank_account.sum_of_funds), "12000")
        self.assertTrue(isinstance(bank_account, BankAccount))
