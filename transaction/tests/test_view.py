"""
Tests for views.
"""

from datetime import datetime, timezone

from django.contrib.auth.models import User
from django.test import Client, TestCase
from rest_framework.reverse import reverse_lazy

from category.models import Category
from transaction.models import Transaction


class TestTransactionCreateView(TestCase):
    """Test transaction create views."""

    def setUp(self):
        """Set up test data."""

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
            category_type="profit",
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
