"""
Tests for views.
"""

from django.http import HttpRequest
from django.test import Client, RequestFactory, TestCase
from rest_framework.reverse import reverse_lazy

from category.factories import CategoryFactory
from users.factories import RandomUserFactory

from ..models import RegularExpenses
from ..views import RegularExpensesDeleteView, RegularExpensesUpdateView


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
        self.success_url = reverse_lazy("expenses_home")
        self.client = Client()
        self.user1 = RandomUserFactory()
        self.user2 = RandomUserFactory()
        self.category1 = CategoryFactory(user=self.user1)
        self.category2 = CategoryFactory(user=self.user2)
        self.request = HttpRequest()
        self.client.force_login(self.user1)

        self.regularExpenses1 = RegularExpenses.objects.create(
            name="Salary",
            category=self.category1,
            sum_amount=122.22,
            description="test description",
            user=self.user1,
        )
        self.regularExpenses3 = RegularExpenses.objects.create(
            name="Salary2",
            category=self.category1,
            sum_amount=1.22,
            description="test description2",
            user=self.user1,
        )
        self.regularExpenses3 = RegularExpenses.objects.create(
            name="Salary3",
            category=self.category2,
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

    def test_uses_correct_template_in_response(self):
        """Ensure that the GET request correctly renders the form template."""

        self.client.force_login(self.user1)
        response = self.client.get(self.success_url, pk=self.user1)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "regular_expenses/expenses_home_page.html")

    def test_update_expenses(self):
        """Checks whether the selected expenses has been updated."""

        updated_data = {
            "name": "Updated",
            "category": self.category1.pk,
            "sum_amount": 200.22,
            "description": "test description nr 2",
        }

        self.client.force_login(self.user1)

        update_url = reverse_lazy("update_expenses", args=[self.regularExpenses1.pk])
        response = self.client.post(update_url, data=updated_data)
        updated_expenses = RegularExpenses.objects.get(pk=self.regularExpenses1.pk)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(updated_expenses.name, "Updated")
        self.assertEqual(updated_expenses.category, self.category1)
        self.assertEqual(updated_expenses.sum_amount, 200.22)
        self.assertEqual(updated_expenses.description, "test description nr 2")


class TestRegularExpensesDeleteView(TestCase):
    """
    Test cases for the expenses delete view.
    These tests verify the behavior of deleting an existing expenses, correct redirections,
    form handling, and database updates
    """

    def setUp(self):
        """Set up test data."""

        self.success_url = reverse_lazy("expenses_home")
        self.client = Client()
        self.user1 = RandomUserFactory()
        self.user2 = RandomUserFactory()
        self.category1 = CategoryFactory(user=self.user1)
        self.category2 = CategoryFactory(user=self.user2)
        self.request = HttpRequest()
        self.client.force_login(self.user1)

        self.regularExpenses1 = RegularExpenses.objects.create(
            name="Salary",
            category=self.category1,
            sum_amount=122.22,
            description="test description",
            user=self.user1,
        )
        self.regularExpenses3 = RegularExpenses.objects.create(
            name="Salary2",
            category=self.category1,
            sum_amount=1.22,
            description="test description2",
            user=self.user1,
        )
        self.regularExpenses3 = RegularExpenses.objects.create(
            name="Salary3",
            category=self.category2,
            sum_amount=99.22,
            description="test description3",
            user=self.user2,
        )

    def test_get_queryset(self):
        """The test simulates user logging in and checks that only the RegularExpenses he has added are available"""

        users = [self.user1, self.user2]

        for user in users:

            self.request.user = user
            view = RegularExpensesDeleteView()
            view.request = self.request
            queryset = view.get_queryset()

            expected_count = RegularExpenses.objects.filter(user=user).count()

            self.assertEqual(queryset.count(), expected_count)

            for expenses in queryset:
                self.assertEqual(expenses.user, user)

    def test_delete_expenses(self):
        """Checks whether the selected expenses has been deleted."""

        self.client.force_login(self.user1)
        delete_url = reverse_lazy("delete_expenses", args=[self.regularExpenses1.pk])
        response = self.client.post(delete_url)

        self.assertEqual(response.status_code, 302)

        with self.assertRaises(RegularExpenses.DoesNotExist):
            RegularExpenses.objects.get(pk=self.regularExpenses1.pk)

        self.assertEqual(RegularExpenses.objects.filter(user=self.user1.id).count(), 1)


class TestRegularExpensesListView(TestCase):
    """
    Test cases for the RegularExpenses list view.
    """

    def setUp(self):
        """
        Set up test data.
        """

        self.factory = RequestFactory()
        self.user = RandomUserFactory()
        self.category1 = CategoryFactory(user=self.user)
        self.url = reverse_lazy("expenses_home")

        self.regularExpenses1 = RegularExpenses.objects.create(
            name="Salary",
            category=self.category1,
            sum_amount=122.22,
            description="test description",
            user=self.user,
        )
        self.regularExpenses3 = RegularExpenses.objects.create(
            name="Salary2",
            category=self.category1,
            sum_amount=1.22,
            description="test description2",
            user=self.user,
        )
        self.regularExpenses3 = RegularExpenses.objects.create(
            name="Salary3",
            category=self.category1,
            sum_amount=99.22,
            description="test description3",
            user=self.user,
        )
