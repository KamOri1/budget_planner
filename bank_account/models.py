from django.contrib.auth.models import User
from django.db import models


class BankAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    number = models.IntegerField()
    sum_of_funds = models.IntegerField()

    def __str__(self) -> str:
        return self.name
