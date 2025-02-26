"""
Tests for views.
"""

from django.http import HttpRequest
from django.test import Client, TestCase
from rest_framework.reverse import reverse_lazy

from users.factories import RandomUserFactory

from ..factories import RandomCategoryFactory
from ..models import Category, CategoryType
from ..views import CategoryDeleteView, CategoryUpdateView


class TestCategoryCreateView(TestCase):
    """Test category create views."""

    def setUp(self):
        """Set up test data.Including a logged-in user"""

        self.client = Client()
        self.user = RandomUserFactory()
        self.client.force_login(self.user)
        self.categoryType = CategoryType.objects.create(
            type="profit",
        )
        self.index_url = reverse_lazy("create_category")
        self.category1 = RandomCategoryFactory(
            user_id=self.user,
            category_type=self.categoryType,
            category_name="Groceries",
        )
        #     (
        #     Category.objects.create(
        #     category_name="Groceries",
        #     category_type=self.categoryType,
        #     user_id=self.user,
        # ))

    def test_form_valid(self):
        """Ensure that the GET request correctly renders the form template."""

        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "category/category_add.html")

    def test_post_valid_data_creates_category(self):
        self.assertEqual(self.category1.category_name, "Groceries")
        self.assertEqual(self.category1.category_type, self.categoryType)
        self.assertEqual(self.category1.user_id, self.user)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.last().user_id, self.user)


class TestCategoryUpdateView(TestCase):
    """
    Test cases for the Category update view.
    These tests verify the behavior of updating an existing Category, correct redirections,
    form handling, and database updates.
    """

    def setUp(self):
        """Set up test data."""
        self.success_url = reverse_lazy("category-home")
        self.categoryType = CategoryType.objects.create(
            type="profit",
        )
        self.client = Client()
        self.user1 = self.user = RandomUserFactory()
        self.user2 = self.user = RandomUserFactory()
        self.request = HttpRequest()
        self.category1 = RandomCategoryFactory(
            user_id=self.user1, category_type=self.categoryType
        )
        self.category2 = RandomCategoryFactory(
            user_id=self.user1, category_type=self.categoryType
        )
        self.category3 = RandomCategoryFactory(
            user_id=self.user2, category_type=self.categoryType
        )

    def test_get_queryset(self):
        """The test simulates user logging in and checks that only the categories he has added are available"""

        users = [self.user1, self.user2]

        for user in users:

            self.request.user = user
            view = CategoryUpdateView()
            view.request = self.request
            queryset = view.get_queryset()

            expected_count = Category.objects.filter(user_id=user).count()

            self.assertEqual(queryset.count(), expected_count)

            for category in queryset:
                self.assertEqual(category.user_id, user)

    def test_uses_correct_template_in_response(self):
        """Ensure that the GET request correctly renders the form template."""

        self.client.force_login(self.user1)
        response = self.client.get(self.success_url, pk=self.user1)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "category/category_home_page.html")

    def test_update_category(self):
        """Checks whether the selected category has been updated."""

        updated_data = {
            "category_name": "Updated Category Name Check",
            "category_type": self.categoryType.pk,
        }

        self.client.force_login(self.user1)

        update_url = reverse_lazy("update_category", args=[self.category1.pk])
        response = self.client.post(update_url, data=updated_data)
        updated_category = Category.objects.get(pk=self.category1.pk)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(updated_category.category_name, "Updated Category Name Check")
        self.assertEqual(updated_category.category_type, self.categoryType)


class TestCategoryDeleteView(TestCase):
    """
    Test cases for the Category delete view.
    These tests verify the behavior of deleting an existing Category, correct redirections,
    form handling, and database updates
    """

    def setUp(self):
        """Set up test data."""
        self.success_url = reverse_lazy("category-home")

        self.client = Client()
        self.user1 = self.user = RandomUserFactory()
        self.user2 = self.user = RandomUserFactory()
        self.request = HttpRequest()
        self.categoryType = CategoryType.objects.create(
            type="profit",
        )
        self.category1 = RandomCategoryFactory(
            user_id=self.user1, category_type=self.categoryType
        )
        self.category2 = RandomCategoryFactory(
            user_id=self.user2, category_type=self.categoryType
        )

    def test_get_queryset(self):
        """The test simulates user logging in and checks that only the categories he has added are available"""

        users = [self.user1, self.user2]

        for user in users:

            self.request.user = user
            view = CategoryDeleteView()
            view.request = self.request
            queryset = view.get_queryset()

            expected_count = Category.objects.filter(user_id=user).count()

            self.assertEqual(queryset.count(), expected_count)

            for category in queryset:
                self.assertEqual(category.user_id, user)

    def test_delete_category(self):
        """Checks whether the selected category has been deleted."""

        self.client.force_login(self.user1)
        delete_url = reverse_lazy("delete_category", args=[self.category1.pk])
        response = self.client.post(delete_url)

        self.assertEqual(response.status_code, 302)

        with self.assertRaises(Category.DoesNotExist):
            Category.objects.get(pk=self.category1.pk)

        self.assertEqual(Category.objects.filter(user_id=self.user1.id).count(), 0)
