from django.urls import path

from billings.views import BillingView

urlpatterns = [
    path("home/", BillingView.as_view(), name="billing"),
]
