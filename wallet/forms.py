from django import forms  # noqa

from .models import Wallet


class CreateWalletForm(forms.ModelForm):

    class Meta:
        model = Wallet
        fields = ["name", "portfolio_value"]


class UpdateWalletForm(forms.ModelForm):

    class Meta:
        model = Wallet
        fields = ["name", "portfolio_value"]
