from rest_framework import serializers

from wallet.models import BankAccount, Wallet


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = "__all__"


class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = "__all__"
