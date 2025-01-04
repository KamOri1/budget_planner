from django.contrib.auth.models import User
from django.db import models


class PossessionStatus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    asset_name = models.CharField(max_length=100)
    asset_value = models.CharField(max_length=100)
    description = models.TextField(max_length=100)

    def __str__(self) -> str:
        return self.asset_name
