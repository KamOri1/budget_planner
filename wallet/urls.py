from django.urls import path

from .views import (
    WalletCreateView,
    WalletDeleteView,
    WalletHomeView,
    WalletListView,
    WalletUpdateView,
)

urlpatterns = [
    path("home/", WalletHomeView.as_view(), name="wallet-home"),
    path("add/", WalletCreateView.as_view(), name="create_wallet"),
    path("update/<pk>", WalletUpdateView.as_view(), name="update_wallet"),
    path("list/<q>", WalletListView.as_view(), name="wallet_list"),
    path("delete/<pk>", WalletDeleteView.as_view(), name="delete_wallet"),
]
