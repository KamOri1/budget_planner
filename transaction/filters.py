import django_filters

from .models import Transaction


class TransactionFilter(django_filters.FilterSet):
    transaction_name = django_filters.CharFilter(lookup_expr="iexact")
    transaction_date = django_filters.DateFilter(
        field_name="transaction_date", lookup_expr="exact"
    )
    sum_amount = django_filters.NumberFilter(field_name="sum_amount", lookup_expr="gte")

    class Meta:
        model = Transaction
        ordering = ["-create_at"]
        fields = ["sum_amount", "transaction_date", "transaction_name"]
