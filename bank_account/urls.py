from django.urls import path

from .views import (
    AccountCreateView,
    AccountDeleteView,
    AccountListView,
    AccountUpdateView,
)

urlpatterns = [
    path("home/", AccountListView.as_view(), name="account-home"),
    path("add/", AccountCreateView.as_view(), name="create_account"),
    path("update/<pk>", AccountUpdateView.as_view(), name="update_account"),
    path("delete/<pk>", AccountDeleteView.as_view(), name="delete_account"),
]
