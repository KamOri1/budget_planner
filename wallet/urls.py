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
    # path("list/wallet", GetAllWallet.as_view(), name="list_wallet"),
    # path("delete/wallet/<int:pk>/", DeleteWallet.as_view(), name="delete_wallet"),
    # path("add/bank_account", BankAccountViewSet.as_view(), name="create_bank_account"),
    # path("list/bank_account", GetAllBankAccount.as_view(), name="list_bank_account"),
    # path(
    #     "delete/bank_account/<int:pk>/",
    #     DeleteBankAccount.as_view(),
    #     name="delete_bank_account",
    # ),
]

# urlpatterns += router.urls
