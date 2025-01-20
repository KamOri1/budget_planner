import django_filters

from .models import RegularExpenses


class RegularExpensesFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="iexact")
    category = django_filters.CharFilter(lookup_expr="iexact")
    sum_amount = django_filters.NumberFilter(field_name="sum_amount", lookup_expr="gte")

    class Meta:
        model = RegularExpenses
        ordering = ["-name"]
        fields = ["sum_amount", "name", "category"]
