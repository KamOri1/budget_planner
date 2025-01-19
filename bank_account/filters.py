import django_filters

from .models import BankAccount


class AccountFilter(django_filters.FilterSet):
    account_name = django_filters.CharFilter(lookup_expr="iexact")
    account_number = django_filters.CharFilter(lookup_expr="iexact")
    sum_of_funds = django_filters.NumberFilter(
        field_name="sum_of_funds", lookup_expr="gte"
    )

    class Meta:
        model = BankAccount
        ordering = ["-account_name"]
        fields = ["sum_of_funds", "account_number", "account_name"]
