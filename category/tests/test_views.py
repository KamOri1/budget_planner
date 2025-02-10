"""
Tests for views.
"""

from django.contrib.auth.models import User
from django.test import Client, TestCase
from rest_framework.reverse import reverse_lazy

from ..models import Category


class TestCategoryCreateView(TestCase):
    """Test category views."""

    def setUp(self):
        """Set up test data.Including a logged-in user"""

        self.client = Client()
        self.user = User.objects.create_user(
            username="Test1", password="password", email="test1@gmail.com"
        )
        self.client.force_login(self.user)
        self.index_url = reverse_lazy("create_category")

    def test_form_valid(self):
        """Ensure that the GET request correctly renders the form template."""

        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "category/category_add.html")

    def test_post_valid_data_creates_category(self):
        data = {
            "category_name": "Test Category",
            "category_type": "profit",
        }
        response = self.client.post(self.index_url, data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.last().category_name, "Test Category")
        self.assertEqual(Category.objects.last().user_id, self.user)
