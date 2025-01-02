from django import forms  # noqa

from .models import Transaction


class CreateTransactionForm(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = ["transaction_name", "category_id", "sum_amount", "description"]
        widgets = {
            "transaction_name": forms.TextInput(
                attrs={"placeholder": "Transaction name"}
            )
        }


class UpdateTransactionForm(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = ["transaction_name", "category_id", "sum_amount", "description"]
        widgets = {"transaction_name": forms.TextInput()}
