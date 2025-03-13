"""
Tests for views.
"""

from django.http import HttpRequest
from django.test import Client, TestCase
from rest_framework.reverse import reverse_lazy

from users.factories import RandomUserFactory

from ..models import BankAccount
from ..views import AccountUpdateView


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


class TestBankAccountUpdateView(TestCase):
    """
    Test cases for the BankAccount update view.
    These tests verify the behavior of updating an existing BankAccount, correct redirections,
    form handling, and database updates.
    """

    def setUp(self):
        """Set up test data."""
        self.client = Client()
        self.user1 = RandomUserFactory()
        self.user2 = RandomUserFactory()
        self.request = HttpRequest()
        self.client.force_login(self.user1)
        self.index_url = reverse_lazy("home_account")
        self.bank_account1 = BankAccount.objects.create(
            user=self.user1, name="PKO", number="12345", sum_of_funds=12000
        )
        self.bank_account2 = BankAccount.objects.create(
            user=self.user2, name="STR", number="5555", sum_of_funds=100
        )

    def test_get_queryset(self):
        """The test simulates user logging in and checks that only the BankAccount he has added are available"""

        users = [self.user1, self.user2]

        for user in users:

            self.request.user = user
            view = AccountUpdateView()
            view.request = self.request
            queryset = view.get_queryset()

            expected_count = BankAccount.objects.filter(user=user).count()

            self.assertEqual(queryset.count(), expected_count)

            for category in queryset:
                self.assertEqual(category.user, user)
