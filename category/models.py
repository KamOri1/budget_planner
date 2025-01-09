from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_type = models.CharField(max_length=100)
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="categories"
    )

    def __str__(self) -> str:
        return self.category_name
