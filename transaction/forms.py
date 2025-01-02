from django import forms  # noqa

from .models import Transaction


class CreateTransactionForm(forms.Form):
    transaction_name = forms.CharField(
        label="Transaction name",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Account name"}
        ),
    )

    sum_amount = forms.FloatField(
        label="Sum amount",
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Sum amount"}
        ),
    )
    category_id = forms.IntegerField(
        label="Category ",
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Category"}
        ),
    )

    description = forms.CharField(
        label="Description",
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "description"}
        ),
    )

    class Meta:
        model = Transaction
        fields = ["transaction_name", "sum_amount", "description", "category_id"]


class UpdateTransactionForm(forms.Form):
    transaction_name = forms.CharField(
        label="Transaction name",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Transaction name"}
        ),
    )

    description = forms.CharField(
        label="Description",
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "description"}
        ),
    )
    sum_amount = forms.IntegerField(
        label="Sum amount",
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Sum amount"}
        ),
    )
    category_id = forms.IntegerField(
        label="Category ",
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Category"}
        ),
    )

    class Meta:
        model = Transaction
        fields = ["transaction_name", "sum_amount", "description", "category_id"]
