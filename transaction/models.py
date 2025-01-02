from django.contrib.auth.models import User
from django.db import models

from category.models import Category


class Transaction(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    sum_amount = models.FloatField()
    description = models.TextField()
    transaction_name = models.TextField(default="")
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.transaction_name
