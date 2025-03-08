import django_filters

from .models import Wallet


class WalletFilter(django_filters.FilterSet):
    wallet_name = django_filters.CharFilter(lookup_expr="iexact")
    portfolio_value = django_filters.NumberFilter(
        field_name="sum_amount", lookup_expr="gte"
    )

    class Meta:
        model = Wallet
        fields = ["name", "portfolio_value"]
