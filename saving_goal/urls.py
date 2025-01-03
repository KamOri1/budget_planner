from django.urls import path

from .views import (
    SavingGoalCreateView,
    SavingGoalDeleteView,
    SavingGoalListView,
    SavingGoalUpdateView,
)

urlpatterns = [
    path("home/", SavingGoalListView.as_view(), name="goal-home"),
    path("add/", SavingGoalCreateView.as_view(), name="create_goal"),
    path("update/<pk>", SavingGoalUpdateView.as_view(), name="update_goal"),
    path("delete/<pk>", SavingGoalDeleteView.as_view(), name="delete_goal"),
]
