"""
Tests for views.
"""

from django.http import HttpRequest
from django.test import Client, TestCase
from rest_framework.reverse import reverse_lazy

from category.factories import CategoryFactory
from users.factories import RandomUserFactory

from ..models import RegularExpenses
from ..views import RegularExpensesUpdateView


class TestRegularExpensesCreateView(TestCase):
    """Test RegularExpenses create views."""

    def setUp(self):
        """Set up test data.Including a logged-in user"""

        self.client = Client()
        self.user = RandomUserFactory()
        self.client.force_login(self.user)
        self.index_url = reverse_lazy("create_expenses")
        self.category = CategoryFactory(user=self.user)
        self.regularExpenses = RegularExpenses.objects.create(
            name="Salary",
            category=self.category,
            sum_amount=122.22,
            description="test description",
            user=self.user,
        )

    def test_form_valid(self):
        """Ensure that the GET request correctly renders the form template."""

        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "regular_expenses/expenses_add.html")

    def test_post_valid_data_creates_expenses(self):
        """The test verifies that the parameters fetched by the POST method are consistent with the stored settings"""
        self.assertEqual(str(self.regularExpenses.name), "Salary")
        self.assertEqual(str(self.regularExpenses.category), self.category.name)
        self.assertEqual(str(self.regularExpenses.sum_amount), "122.22")
        self.assertEqual(str(self.regularExpenses.description), "test description")
        self.assertEqual(self.regularExpenses.user_id, self.user.id)
        self.assertTrue(isinstance(self.regularExpenses, RegularExpenses))


class TestRegularExpensesUpdateView(TestCase):
    """
    Test cases for the regularExpenses update view.
    These tests verify the behavior of updating an existing regularExpenses, correct redirections,
    form handling, and database updates.
    """

    def setUp(self):
        """Set up test data."""
        self.success_url = reverse_lazy("create_expenses")
        self.client = Client()
        self.user1 = RandomUserFactory()
        self.user2 = RandomUserFactory()
        self.request = HttpRequest()
        self.client.force_login(self.user1)
        self.regularExpenses1 = RegularExpenses.objects.create(
            name="Salary",
            category=CategoryFactory(user=self.user1),
            sum_amount=122.22,
            description="test description",
            user=self.user1,
        )
        self.regularExpenses3 = RegularExpenses.objects.create(
            name="Salary2",
            category=CategoryFactory(user=self.user1),
            sum_amount=1.22,
            description="test description2",
            user=self.user1,
        )
        self.regularExpenses1 = RegularExpenses.objects.create(
            name="Salary3",
            category=CategoryFactory(user=self.user2),
            sum_amount=99.22,
            description="test description3",
            user=self.user2,
        )

    def test_get_queryset(self):
        """The test simulates user logging in and checks that only the RegularExpenses he has added are available"""

        users = [self.user1, self.user2]

        for user in users:

            self.request.user = user
            view = RegularExpensesUpdateView()
            view.request = self.request
            queryset = view.get_queryset()

            expected_count = RegularExpenses.objects.filter(user=user).count()

            self.assertEqual(queryset.count(), expected_count)

            for expenses in queryset:
                self.assertEqual(expenses.user, user)
