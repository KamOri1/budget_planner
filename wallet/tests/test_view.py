"""
Tests for views.
"""

from django.test import Client, TestCase
from rest_framework.reverse import reverse_lazy

from users.factories import RandomUserFactory
from wallet.models import Wallet


class TestWalletCreateView(TestCase):
    """Test wallet create views."""

    def setUp(self):
        """Set up test data."""

        self.success_url = reverse_lazy("wallet-home")
        self.index_url = reverse_lazy("create_wallet")
        self.client = Client()
        self.user = RandomUserFactory()
        self.client.force_login(self.user)

    def test_form_valid(self):
        """Ensure that the GET request correctly renders the form template."""

        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "wallet/wallet_add.html")

    def test_post_valid_data_creates_wallet(self):
        """Test create Wallet"""

        wallet = {
            "user": self.user,
            "name": "smart wallet",
            "portfolio_value": 433,
        }
        response = self.client.post(self.index_url, wallet, force=True)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Wallet.objects.count(), 1)
        self.assertEqual(Wallet.objects.last().name, "smart wallet")
        self.assertEqual(Wallet.objects.last().user, self.user)
        self.assertEqual(Wallet.objects.last().portfolio_value, 433)
