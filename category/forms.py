from django import forms  # noqa

from .models import Category


class CreateCategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ["category_name", "category_type"]


class UpdateCategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ["category_name", "category_type"]
