from django.urls import path

from .views import (
    RegularExpensesCreateView,
    RegularExpensesDeleteView,
    RegularExpensesListView,
    RegularExpensesUpdateView,
)

urlpatterns = [
    path("home/", RegularExpensesListView.as_view(), name="expenses_home"),
    path("add/", RegularExpensesCreateView.as_view(), name="create_expenses"),
    path("update/<pk>", RegularExpensesUpdateView.as_view(), name="update_expenses"),
    path("delete/<pk>", RegularExpensesDeleteView.as_view(), name="delete_expenses"),
]
