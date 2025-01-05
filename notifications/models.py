from django.contrib.auth.models import User
from django.db import models

from notifications_type.models import NotificationType


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.ForeignKey(NotificationType, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    message = models.TextField()

    def __str__(self):
        return self.name
