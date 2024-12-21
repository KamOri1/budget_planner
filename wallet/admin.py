from django.contrib import admin

from wallet.models import BankAccount, Wallet

admin.site.register(Wallet)
admin.site.register(BankAccount)
