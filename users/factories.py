import factory
from django.contrib.auth.models import User
from faker import Faker

fake = Faker()


class RandomUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ("username",)

    username = factory.Faker("user_name")
    email = factory.LazyAttribute(lambda obj: f"{obj.username}@example.com")
    password = factory.PostGenerationMethodCall("set_password", "password123")
    is_active = True
    is_staff = False
    is_superuser = False
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")

    # @factory.post_generation
    # def password(self, create, extracted, **kwargs):
    #     password = extracted or fake.password()
    #     self.set_password(password)
