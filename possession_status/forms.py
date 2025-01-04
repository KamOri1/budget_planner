from django import forms  # noqa

from .models import PossessionStatus


class CreatePossessionStatusForm(forms.ModelForm):

    class Meta:
        model = PossessionStatus
        fields = ["asset_name", "asset_value", "description"]


class UpdatePossessionStatusForm(forms.ModelForm):

    class Meta:
        model = PossessionStatus
        fields = ["asset_name", "asset_value", "description"]
