from django.contrib.auth.models import User
from django.db import models


class SavingGoal(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="saving_goals"
    )
    description = models.TextField()
    target_date = models.DateField()
    target_amount = models.IntegerField()
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.description
