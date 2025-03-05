import django_filters

from .models import Category


class CategoryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="iexact")
    type = django_filters.CharFilter(lookup_expr="iexact")

    class Meta:
        model = Category
        ordering = ["-name"]
        fields = ["type", "name"]
