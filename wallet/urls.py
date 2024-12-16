from django.urls import path
from rest_framework import routers

from .views import (  # DeleteWallet,; GetAllWallet,
    BankAccountViewSet,
    DeleteBankAccount,
    GetAllBankAccount,
    WalletViewSet,
)

router = routers.SimpleRouter()
router.register(r"wallets", WalletViewSet)

urlpatterns = [
    # path("add/wallet", WalletViewSet.as_view(), name="create_wallet"),
    # path("list/wallet", GetAllWallet.as_view(), name="list_wallet"),
    # path("delete/wallet/<int:pk>/", DeleteWallet.as_view(), name="delete_wallet"),
    path("add/bank_account", BankAccountViewSet.as_view(), name="create_bank_account"),
    path("list/bank_account", GetAllBankAccount.as_view(), name="list_bank_account"),
    path(
        "delete/bank_account/<int:pk>/",
        DeleteBankAccount.as_view(),
        name="delete_bank_account",
    ),
]

urlpatterns += router.urls
