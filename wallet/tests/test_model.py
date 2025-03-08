"""
Tests for model.
"""

from datetime import datetime, timezone

from django.contrib.auth.models import User
from django.test import TestCase

from ..models import Wallet


class TestModels(TestCase):
    """Test transaction model."""

    def setUp(self):
        """Set up test data."""

        self.user = User.objects.create_user(
            username="Test", password="password", email="test@gmail.com"
        )

        self.transaction_date_value = datetime(
            2025, 2, 10, 11, 35, 10, tzinfo=timezone.utc
        )

    def test_model_Wallet(self):
        """Test create Wallet"""

        wallet = Wallet.objects.create(
            user=self.user,
            name="Test1",
            portfolio_value=12330,
        )
        self.assertEqual(str(wallet.user), self.user.username)
        self.assertEqual(wallet.name, "Test1")
        self.assertEqual(wallet.portfolio_value, 12330)
        self.assertTrue(isinstance(wallet, Wallet))
