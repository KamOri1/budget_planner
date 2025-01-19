import django_filters

from .models import Notification


class NotificationFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="iexact")
    type = django_filters.CharFilter(lookup_expr="iexact")

    class Meta:
        model = Notification
        ordering = ["-name"]
        fields = ["name", "type"]
