from django import forms  # noqa

from .models import Wallet


class WalletForm(forms.Form):
    wallet_name = forms.CharField(
        label="Nazwa portfela",  # Dodano etykietę
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Wallet name"}
        ),
    )
    portfolio_value = forms.IntegerField(
        label="Wartość portfela",  # Dodano etykietę
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Portfolio value"}
        ),
    )

    class Meta:
        model = Wallet
        fields = ["wallet_name", "portfolio_value"]