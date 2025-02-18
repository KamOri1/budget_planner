from django.contrib.auth.models import User
from django.db import models


class CategoryType(models.Model):
    type = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.type


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_type = models.ForeignKey(CategoryType, on_delete=models.PROTECT)
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="categories"
    )

    def __str__(self) -> str:
        return self.category_name
