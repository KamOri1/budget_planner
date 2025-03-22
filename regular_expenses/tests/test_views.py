"""
Tests for views.
"""

from django.test import Client, TestCase
from rest_framework.reverse import reverse_lazy

from category.factories import CategoryFactory
from users.factories import RandomUserFactory

from ..models import RegularExpenses


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
