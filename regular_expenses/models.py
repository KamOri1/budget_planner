from django.contrib.auth.models import User
from django.db import models

from category.models import Category


class RegularExpenses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sum_amount = models.FloatField()
    name = models.CharField(default="", max_length=100)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name
