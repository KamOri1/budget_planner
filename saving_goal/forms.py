from django import forms  # noqa

from .models import SavingGoal


class CreateSavingGoalForm(forms.ModelForm):

    class Meta:
        model = SavingGoal
        fields = ["description", "target_date", "target_amount", "name"]
        widgets = {
            "target_date": forms.DateInput(attrs={"type": "date"}),
        }


class UpdateSavingGoalForm(forms.ModelForm):

    class Meta:
        model = SavingGoal
        fields = ["description", "target_date", "target_amount", "name"]
        widgets = {
            "target_date": forms.DateInput(attrs={"type": "date"}),
        }
