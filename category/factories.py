import secrets

import factory
from faker import Faker

from .models import Category, CategoryType

fake = Faker()

CATEGORY_NAMES = [
    "food",
    "car",
]

CATEGORY_TYPES = ["1", "2"]


class CategoryTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CategoryType

    type = factory.LazyAttribute(lambda x: secrets.choice(CATEGORY_TYPES))


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.LazyAttribute(lambda x: secrets.choice(CATEGORY_NAMES))
    type = factory.SubFactory(CategoryTypeFactory)
