from django.urls import path

from .views import (
    TransactionCreateView,
    TransactionDeleteView,
    TransactionHomeView,
    TransactionListView,
    TransactionUpdateView,
)

urlpatterns = [
    path("home/", TransactionHomeView.as_view(), name="transaction-home"),
    path("add/", TransactionCreateView.as_view(), name="create_transaction"),
    path("update/<pk>", TransactionUpdateView.as_view(), name="update_transaction"),
    path("list/<q>", TransactionListView.as_view(), name="transaction_list"),
    path("delete/<pk>", TransactionDeleteView.as_view(), name="delete_transaction"),
]
