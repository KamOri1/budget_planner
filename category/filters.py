import django_filters

from .models import Category


class CategoryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="exact")
    type = django_filters.CharFilter(lookup_expr="exact", field_name="type__type")

    class Meta:
        model = Category
        ordering = ["-name"]
        fields = ["type", "name"]
