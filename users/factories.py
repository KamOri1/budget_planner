import factory
from django.contrib.auth.models import User
from faker import Faker

fake = Faker()


class RandomUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    email = factory.Faker("email")

    @factory.post_generation
    def password(self, create, extracted, **kwargs):
        password = extracted or fake.password()
        self.set_password(password)
