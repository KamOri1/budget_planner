from django.urls import path

from .views import (
    AccountCreateView,
    AccountDeleteView,
    AccountHomeView,
    AccountListView,
    AccountUpdateView,
)

urlpatterns = [
    path("home/", AccountHomeView.as_view(), name="account-home"),
    path("add/", AccountCreateView.as_view(), name="create_account"),
    path("update/<pk>", AccountUpdateView.as_view(), name="update_account"),
    path("list/<q>", AccountListView.as_view(), name="account_list"),
    path("delete/<pk>", AccountDeleteView.as_view(), name="delete_account"),
]
