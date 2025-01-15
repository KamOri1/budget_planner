import django_filters

from .models import Transaction


class TransactionFilter(django_filters.FilterSet):
    transaction_name = django_filters.CharFilter(lookup_expr="iexact")
    transaction_date = django_filters.DateFilter(field_name="date", lookup_expr="gte")
    sum_amount = django_filters.NumberFilter(field_name="sum_amount", lookup_expr="gte")

    class Meta:
        model = Transaction
        fields = ["sum_amount", "transaction_date", "transaction_name"]
