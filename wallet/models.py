from django.contrib.auth.models import User
from django.db import models


class Wallet(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    wallet_name = models.CharField(max_length=100)
    portfolio_value = models.IntegerField()
