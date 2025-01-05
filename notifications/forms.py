from django import forms  # noqa

from .models import Notification


class CreateNotificationForm(forms.ModelForm):

    class Meta:
        model = Notification
        fields = ["name", "type", "message"]


class UpdateNotificationForm(forms.ModelForm):

    class Meta:
        model = Notification
        fields = ["name", "type", "message"]
