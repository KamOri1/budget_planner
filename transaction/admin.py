from django.contrib import admin

from .models import Transaction


class TransactionAdmin(admin.ModelAdmin):
    list_display = ("pk", "transaction_name", "transaction_date")


admin.site.register(Transaction, TransactionAdmin)
