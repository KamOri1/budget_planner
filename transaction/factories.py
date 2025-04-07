import secrets

import factory
from django.utils import timezone
from faker import Faker

from category.factories import CategoryFactory

from .models import Transaction

fake = Faker()

TRANSACTION_NAME = ["food", "shopping", "vacation", "fun", "home"]


class TransactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Transaction

    category = factory.SubFactory(CategoryFactory)
    sum_amount = factory.Faker(
        "pydecimal", left_digits=5, right_digits=2, positive=True
    )
    description = factory.Faker("paragraph", nb_sentences=3, variable_nb_sentences=True)
    transaction_name = factory.LazyAttribute(lambda x: secrets.choice(TRANSACTION_NAME))
    create_at = factory.Faker(
        "past_datetime", start_date="-30d", tzinfo=timezone.get_current_timezone()
    )
    transaction_date = factory.Faker(
        "past_datetime", start_date="-30d", tzinfo=timezone.get_current_timezone()
    )
