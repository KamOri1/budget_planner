from django.contrib.auth.models import User
from django.test import Client, TestCase
from rest_framework.reverse import reverse_lazy

from .models import Category


class TestModels(TestCase):
    def test_model_Category(self):
        user = User.objects.create_user(
            username="Test", password="password", email="test@gmail.com"
        )

        category = Category.objects.create(
            user_id=user,
            category_name="Salary",
            category_type="profit",
        )

        self.assertEqual(str(category.user_id), user.username)
        self.assertEqual(str(category), "Salary")
        self.assertEqual(str(category.category_type), "profit")
        self.assertTrue(isinstance(category, Category))


class TestView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="Test1", password="password", email="test1@gmail.com"
        )
        self.client.force_login(self.user)  # Log the user in
        self.index_url = reverse_lazy("create_category")  # Use reverse

    def test_CategoryCreateView(self):
        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "category/category_add.html")

    def test_add_category_POST(self):
        data = {
            "category_name": "Test Category",
            "category_type": "profit",
        }
        response = self.client.post(self.index_url, data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.last().category_name, "Test Category")
        self.assertEqual(Category.objects.last().user_id, self.user)
