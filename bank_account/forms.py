from django import forms  # noqa

from .models import BankAccount


class CreateAccountForm(forms.Form):
    account_name = forms.CharField(
        label="Account name",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Account name"}
        ),
    )
    account_number = forms.IntegerField(
        label="Account number",
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Account number"}
        ),
    )
    sum_of_funds = forms.IntegerField(
        label="Sum of funds",
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Sum of funds"}
        ),
    )

    class Meta:
        model = BankAccount
        fields = ["name", "number", "sum_of_funds"]


class UpdateAccountForm(forms.Form):
    account_name = forms.CharField(
        label="Account name",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Account name"}
        ),
    )
    account_number = forms.IntegerField(
        label="Account number",
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Account number"}
        ),
    )
    sum_of_funds = forms.IntegerField(
        label="Sum of funds",
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Sum of funds"}
        ),
    )

    class Meta:
        model = BankAccount
        fields = ["name", "number", "sum_of_funds"]
