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
            "transaction_date": forms.DateTimeInput(attrs={"type": "datetime-local"}),
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
        widgets = {
            "transaction_date": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }
