import django_filters

from .models import Category


class CategoryFilter(django_filters.FilterSet):
    category_name = django_filters.CharFilter(lookup_expr="iexact")
    category_type = django_filters.CharFilter(lookup_expr="iexact")

    class Meta:
        model = Category
        ordering = ["-category_name"]
        fields = ["category_type", "category_name"]
