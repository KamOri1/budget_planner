from rest_framework import generics, permissions
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from api.serializers import BankAccountSerializer, WalletSerializer
from bank_account.models import BankAccount
from wallet.models import Wallet


class WalletViewSet(
    GenericViewSet, CreateModelMixin, ListModelMixin, DestroyModelMixin
):
    serializer_class = WalletSerializer
    queryset = Wallet.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# class WalletViewSet(generics.CreateAPIView):
#     serializer_class = WalletSerializer
#     queryset = Wallet.objects.all()
#
#
# class GetAllWallet(generics.ListAPIView):
#     serializer_class = WalletSerializer
#     queryset = Wallet.objects.all()
#
#
# class DeleteWallet(generics.DestroyAPIView):
#     serializer_class = WalletSerializer
#     queryset = Wallet.objects.all()
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BankAccountViewSet(generics.CreateAPIView):
    serializer_class = BankAccountSerializer
    queryset = BankAccount.objects.all()


class GetAllBankAccount(generics.ListAPIView):
    serializer_class = BankAccountSerializer
    queryset = BankAccount.objects.all()


class DeleteBankAccount(generics.DestroyAPIView):
    serializer_class = BankAccountSerializer
    queryset = BankAccount.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
