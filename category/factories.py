import factory
from faker import Faker

from .models import Category

fake = Faker()


class RandomCategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    category_name = factory.Faker("word")
    category_type = factory.LazyAttribute(
        lambda x: fake.random_element(elements=("profit", "cost"))
    )
