from django import forms  # noqa

from .models import Wallet


class CreateWalletForm(forms.Form):
    wallet_name = forms.CharField(
        label="Wallet name",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Wallet name"}
        ),
    )
    portfolio_value = forms.IntegerField(
        label="Portfolio value",
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Portfolio value"}
        ),
    )

    class Meta:
        model = Wallet
        fields = ["wallet_name", "portfolio_value"]


class UpdateWalletForm(forms.Form):
    wallet_id = forms.IntegerField(
        label="Portfolio value",
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Portfolio value"}
        ),
    )

    class Meta:
        model = Wallet
        fields = ["wallet_id"]
