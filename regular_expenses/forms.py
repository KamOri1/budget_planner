from django import forms  # noqa

from .models import RegularExpenses


class CreateRegularExpensesForm(forms.ModelForm):

    class Meta:
        model = RegularExpenses
        fields = ["category", "sum_amount", "name", "description"]


class UpdateRegularExpensesForm(forms.ModelForm):

    class Meta:
        model = RegularExpenses
        fields = ["category", "sum_amount", "name", "description"]
