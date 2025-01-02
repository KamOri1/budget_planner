from django.contrib.auth.models import User
from django.db import models


class Wallet(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    wallet_name = models.CharField(max_length=50, unique=True)
    portfolio_value = models.IntegerField()

    def __str__(self):
        return self.wallet_name
