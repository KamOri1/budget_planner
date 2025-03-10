import django_filters

from .models import BankAccount


class AccountFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="iexact")
    number = django_filters.CharFilter(lookup_expr="iexact")
    sum_of_funds = django_filters.NumberFilter(
        field_name="sum_of_funds", lookup_expr="gte"
    )

    class Meta:
        model = BankAccount
        ordering = ["-name"]
        fields = ["sum_of_funds", "number", "name"]
