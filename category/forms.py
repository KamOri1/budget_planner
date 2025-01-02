from django import forms  # noqa

from .models import Category


class CreateCategoryForm(forms.Form):
    category_name = forms.CharField(
        label="Category name",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Category name"}
        ),
    )
    category_type = forms.IntegerField(
        label="Category type",
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Category type"}
        ),
    )

    class Meta:
        model = Category
        fields = ["category_name", "category_type"]


class UpdateCategoryForm(forms.Form):
    category_name = forms.CharField(
        label="Category name",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Category name"}
        ),
    )
    category_type = forms.IntegerField(
        label="Category type",
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Category type"}
        ),
    )

    class Meta:
        model = Category
        fields = ["category_name", "category_type"]
