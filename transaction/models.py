from django.contrib.auth.models import User
from django.db import models

from category.models import Category


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sum_amount = models.FloatField()
    description = models.TextField()
    transaction_name = models.CharField(default="", max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    transaction_date = models.DateTimeField()

    def __str__(self) -> str:
        return self.transaction_name
