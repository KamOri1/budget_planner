from django.urls import path

from .views import (
    TransactionCreateView,
    TransactionDeleteView,
    TransactionListView,
    TransactionUpdateView,
)

urlpatterns = [
    path("home/", TransactionListView.as_view(), name="transaction-home"),
    path("add/", TransactionCreateView.as_view(), name="create_transaction"),
    path("update/<pk>", TransactionUpdateView.as_view(), name="update_transaction"),
    path("delete/<pk>", TransactionDeleteView.as_view(), name="delete_transaction"),
]
