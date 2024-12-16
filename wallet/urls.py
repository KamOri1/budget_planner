from django.urls import path

from .views import BankAccountViewSet, WalletViewSet

urlpatterns = [
    path("add/wallet", WalletViewSet.as_view(), name="create_wallet"),
    path("add/bank_account", BankAccountViewSet.as_view(), name="create_bank_account"),
]
