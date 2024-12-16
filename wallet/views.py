from rest_framework import permissions
from rest_framework.viewsets import generics

from wallet.models import BankAccount, Wallet

from .serializers import BankAccountSerializer, WalletSerializer


class WalletViewSet(generics.CreateAPIView):
    serializer_class = WalletSerializer
    queryset = Wallet.objects.all()


class GetAllWallet(generics.ListAPIView):
    serializer_class = WalletSerializer
    queryset = Wallet.objects.all()


class DeleteWallet(generics.DestroyAPIView):
    serializer_class = WalletSerializer
    queryset = Wallet.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


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
