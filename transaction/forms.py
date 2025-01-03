from django import forms  # noqa

from .models import Transaction


class CreateTransactionForm(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = [
            "transaction_name",
            "transaction_date",
            "category_id",
            "sum_amount",
            "description",
        ]
        widgets = {
            "transaction_name": forms.TextInput(
                attrs={"placeholder": "Transaction name"}
            ),
            "transaction_date": forms.DateInput(attrs={"type": "date"}),
        }


class UpdateTransactionForm(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = [
            "transaction_name",
            "transaction_date",
            "category_id",
            "sum_amount",
            "description",
        ]
        widgets = {"transaction_name": forms.TextInput()}
