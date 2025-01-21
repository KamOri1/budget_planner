import django_filters

from .models import SavingGoal


class SavingGoalFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="iexact")
    target_date = django_filters.DateFilter(field_name="date", lookup_expr="gte")
    target_amount = django_filters.NumberFilter(
        field_name="target_amount", lookup_expr="gte"
    )

    class Meta:
        model = SavingGoal
        ordering = ["-target_date"]
        fields = ["name", "target_date", "target_amount"]
