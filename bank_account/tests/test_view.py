"""
Tests for views.
"""

from django.test import Client, TestCase
from rest_framework.reverse import reverse_lazy

from users.factories import RandomUserFactory

from ..models import BankAccount


class TestBankAccountCreateView(TestCase):
    """Test BankAccount create views."""

    def setUp(self):
        """Set up test data.Including a logged-in user"""

        self.client = Client()
        self.user = RandomUserFactory()
        self.client.force_login(self.user)
        self.index_url = reverse_lazy("create_account")
        self.bank_account = BankAccount.objects.create(
            user=self.user, name="PKO", number="12345", sum_of_funds=12000
        )

    def test_form_valid(self):
        """Ensure that the GET request correctly renders the form template."""

        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bank_account/account_add.html")

    def test_post_valid_data_creates_BankAccount(self):
        self.assertEqual(self.bank_account.name, "PKO")
        self.assertEqual(self.bank_account.number, "12345")
        self.assertEqual(self.bank_account.sum_of_funds, 12000)
        self.assertEqual(self.bank_account.user, self.user)
        self.assertEqual(BankAccount.objects.count(), 1)
        self.assertEqual(BankAccount.objects.last().user, self.user)
