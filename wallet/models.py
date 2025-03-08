from django.contrib.auth.models import User
from django.db import models


class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    portfolio_value = models.IntegerField()

    def __str__(self) -> str:
        return self.name
