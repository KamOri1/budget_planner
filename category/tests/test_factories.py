from django.test import TestCase

from ..factories import CategoryFactory
from ..models import Category, CategoryType


class TestCategoryFactory(TestCase):
    def test_single_object_create(self):
        category = CategoryFactory.create()

        self.assertTrue(isinstance(category, Category))
        self.assertEqual(1, Category.objects.count())
        self.assertEqual(1, CategoryType.objects.count())

    def test_batch_object_create(self):
        categories = CategoryFactory.create_batch(5)

        self.assertEqual(5, len(categories))
        self.assertEqual(5, Category.objects.count())
        self.assertEqual(5, CategoryType.objects.count())
