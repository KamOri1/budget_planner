from django.urls import path

from .views import (
    PossessionsCreateView,
    PossessionsDeleteView,
    PossessionsListView,
    PossessionsUpdateView,
)

urlpatterns = [
    path("home/", PossessionsListView.as_view(), name="possessions_home"),
    path("add/", PossessionsCreateView.as_view(), name="create_possessions"),
    path("update/<pk>", PossessionsUpdateView.as_view(), name="update_possessions"),
    path("delete/<pk>", PossessionsDeleteView.as_view(), name="delete_possessions"),
]
