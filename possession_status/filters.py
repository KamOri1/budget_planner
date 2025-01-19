import django_filters

from .models import PossessionStatus


class PossessionStatusFilter(django_filters.FilterSet):
    asset_name = django_filters.CharFilter(lookup_expr="iexact")
    asset_value = django_filters.NumberFilter(
        field_name="sum_amount", lookup_expr="gte"
    )

    class Meta:
        model = PossessionStatus
        ordering = ["-asset_name"]
        fields = ["asset_name", "asset_value"]
