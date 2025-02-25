"""
Tests for views.
"""

from django.contrib.auth.models import User
from django.test import Client, TestCase
from rest_framework.reverse import reverse_lazy

from wallet.models import Wallet


class TestWalletCreateView(TestCase):
    """Test wallet create views."""

    def setUp(self):
        """Set up test data."""

        self.success_url = reverse_lazy("wallet-home")
        self.index_url = reverse_lazy("create_wallet")
        self.client = Client()
        self.user = User.objects.create_user(
            username="Test1", password="password", email="test1@gmail.com"
        )
        self.client.force_login(self.user)

    def test_form_valid(self):
        """Ensure that the GET request correctly renders the form template."""

        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "wallet/wallet_add.html")

    def test_post_valid_data_creates_wallet(self):
        """Test create Wallet"""

        wallet = {
            "user_id": self.user.id,
            "wallet_name": "smart wallet",
            "portfolio_value": 433,
        }
        response = self.client.post(self.index_url, wallet, force=True)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Wallet.objects.count(), 1)
        self.assertEqual(Wallet.objects.last().wallet_name, "smart wallet")
        self.assertEqual(Wallet.objects.last().user_id, self.user)
        self.assertEqual(Wallet.objects.last().portfolio_value, 433)
