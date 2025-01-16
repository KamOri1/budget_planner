from django.urls import path

from .views import WalletCreateView, WalletDeleteView, WalletListView, WalletUpdateView

urlpatterns = [
    path("", WalletListView.as_view(), name="wallet-home"),
    path("add/", WalletCreateView.as_view(), name="create_wallet"),
    path("update/<pk>", WalletUpdateView.as_view(), name="update_wallet"),
    path("delete/<pk>", WalletDeleteView.as_view(), name="delete_wallet"),
]
