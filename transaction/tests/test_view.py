"""
Tests for views.
"""

from datetime import datetime, timezone

from django.contrib.auth.models import User
from django.http import HttpRequest
from django.test import Client, TestCase
from rest_framework.reverse import reverse_lazy

from category.models import Category, CategoryType
from transaction.models import Transaction
from transaction.views import TransactionDeleteView, TransactionUpdateView


class TestTransactionCreateView(TestCase):
    """Test transaction create views."""

    def setUp(self):
        """Set up test data."""

        self.categoryType = CategoryType.objects.create(
            type="profit",
        )
        self.success_url = reverse_lazy("transaction-home")
        self.index_url = reverse_lazy("create_transaction")
        self.client = Client()
        self.user = User.objects.create_user(
            username="Test1", password="password", email="test1@gmail.com"
        )
        self.client.force_login(self.user)
        self.category = Category.objects.create(
            user_id=self.user,
            category_name="Salary",
            category_type=self.categoryType,
        )
        self.transaction_date_value = datetime(
            2025, 2, 10, 11, 35, 10, tzinfo=timezone.utc
        )

    def test_form_valid(self):
        """Ensure that the GET request correctly renders the form template."""

        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "transaction/transaction_add.html")

    def test_post_valid_data_creates_transaction(self):
        """Test create Transaction"""

        transaction = {
            "user_id": self.user.id,
            "category_id": self.category.id,
            "sum_amount": 433.33,
            "description": "something to test",
            "transaction_name": "Shopping",
            "transaction_date": self.transaction_date_value,
        }
        response = self.client.post(self.index_url, transaction, force=True)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Transaction.objects.count(), 1)
        self.assertEqual(Transaction.objects.last().transaction_name, "Shopping")
        self.assertEqual(Transaction.objects.last().user_id, self.user)
        self.assertEqual(Transaction.objects.last().category_id, self.category)
        self.assertEqual(
            Transaction.objects.last().transaction_date, self.transaction_date_value
        )


class TestTransactionUpdateView(TestCase):
    """
    Test cases for the Transaction update view.
    These tests verify the behavior of updating an existing transaction, correct redirections,
    form handling, and database updates.
    """

    def setUp(self):
        """Set up test data."""
        self.categoryType = CategoryType.objects.create(
            type="profit",
        )
        self.success_url = reverse_lazy("transaction-home")
        self.index_url = reverse_lazy("create_transaction")
        self.client = Client()
        self.user = User.objects.create_user(
            username="Test1", password="password", email="test1@gmail.com"
        )
        self.client.force_login(self.user)
        self.category = Category.objects.create(
            user_id=self.user,
            category_name="test",
            category_type=self.categoryType,
        )
        self.transaction_date_value = datetime(
            2025, 2, 10, 11, 35, 10, tzinfo=timezone.utc
        )

        self.request = HttpRequest()

    def test_get_queryset(self):
        """The test simulates user logging in and checks that only the transaction he has added are available"""

        self.request.user = self.user
        view = TransactionUpdateView()
        view.request = self.request
        queryset = view.get_queryset()

        expected_count = Transaction.objects.filter(user_id=self.user).count()

        self.assertEqual(queryset.count(), expected_count)

        for transaction in queryset:
            self.assertEqual(transaction.user_id, self.user)

    def test_uses_correct_template_in_response(self):
        """Ensure that the GET request correctly renders the form template."""

        response = self.client.get(self.success_url, pk=self.user)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "transaction/transaction_home_page.html")

    def test_update_transaction(self):
        """Checks whether the selected transaction has been updated."""

        transaction = Transaction.objects.create(
            user_id=self.user,
            category_id=self.category,
            sum_amount=433.33,
            description="something to test",
            transaction_name="Shopping",
            transaction_date=self.transaction_date_value,
        )
        updated_data = {
            "user_id": self.user.id,
            "category_id": self.category.id,
            "sum_amount": 10.45,
            "description": "Another description",
            "transaction_name": "Shopping",
            "transaction_date": self.transaction_date_value,
        }

        self.client.force_login(self.user)

        update_url = reverse_lazy("update_transaction", args=[transaction.pk])
        response = self.client.post(update_url, data=updated_data)
        updated_transaction = Transaction.objects.get(pk=transaction.pk)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(updated_transaction.description, "Another description")
        self.assertEqual(updated_transaction.sum_amount, 10.45)


class TestCategoryDeleteView(TestCase):
    """
    Test cases for the Transaction delete view.
    These tests verify the behavior of deleting an existing Transaction, correct redirections,
    form handling, and database updates
    """

    def setUp(self):
        """Set up test data."""
        self.categoryType = CategoryType.objects.create(
            type="profit",
        )
        self.success_url = reverse_lazy("transaction-home")
        self.index_url = reverse_lazy("create_transaction")
        self.client = Client()
        self.user = User.objects.create_user(
            username="Test1", password="password", email="test1@gmail.com"
        )
        self.client.force_login(self.user)
        self.category = Category.objects.create(
            user_id=self.user,
            category_name="test",
            category_type=self.categoryType,
        )
        self.transaction_date_value = datetime(
            2025, 2, 10, 11, 35, 10, tzinfo=timezone.utc
        )

        self.transaction = Transaction.objects.create(
            user_id=self.user,
            category_id=self.category,
            sum_amount=433.33,
            description="something to test",
            transaction_name="Shopping",
            transaction_date=self.transaction_date_value,
        )
        self.request = HttpRequest()

    def test_get_queryset(self):
        """The test simulates user logging in and checks that only the categories he has added are available"""

        self.request.user = self.user
        view = TransactionDeleteView()
        view.request = self.request
        queryset = view.get_queryset()

        expected_count = Transaction.objects.filter(user_id=self.user).count()

        self.assertEqual(queryset.count(), expected_count)

        for transaction in queryset:
            self.assertEqual(transaction.user_id, self.user)

    def test_delete_transaction(self):
        """Checks whether the selected transaction has been deleted."""

        self.client.force_login(self.user)
        delete_url = reverse_lazy("delete_transaction", args=[self.transaction.pk])
        response = self.client.post(delete_url)

        self.assertEqual(response.status_code, 302)

        with self.assertRaises(Transaction.DoesNotExist):
            Transaction.objects.get(pk=self.transaction.pk)

        self.assertEqual(Transaction.objects.filter(user_id=self.user.id).count(), 0)
