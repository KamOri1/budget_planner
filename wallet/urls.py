from django.urls import path

from .views import WalletCreateView, WalletListView

urlpatterns = [
    path(
        "list/",
        WalletListView.as_view(template_name="wallet/wallet_home_page.html"),
        name="wallet-home",
    ),
    path("add/", WalletCreateView.as_view(), name="create_wallet"),
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
