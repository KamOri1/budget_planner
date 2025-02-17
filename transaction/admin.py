from django.contrib import admin

from .models import Transaction


class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "transaction_name",
        "transaction_date",
        "create_at",
    )  # , "transaction_date", "create_at"


admin.site.register(Transaction, TransactionAdmin)
