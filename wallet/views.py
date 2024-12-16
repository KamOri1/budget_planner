from rest_framework.viewsets import generics

from wallet.models import BankAccount, Wallet

from .serializers import BankAccountSerializer, WalletSerializer


class WalletViewSet(generics.CreateAPIView):
    serializer_class = WalletSerializer
    queryset = Wallet.objects.all()


class BankAccountViewSet(generics.CreateAPIView):
    serializer_class = BankAccountSerializer
    queryset = BankAccount.objects.all()
