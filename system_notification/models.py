from django.db import models

from notifications_type.models import NotificationType


class SystemNotification(models.Model):
    type = models.ForeignKey(NotificationType, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    message = models.TextField()

    def __str__(self):
        return self.name
