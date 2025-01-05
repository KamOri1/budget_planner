from django.urls import path

from .views import (
    NotificationCreateView,
    NotificationDeleteView,
    NotificationListView,
    NotificationUpdateView,
)

urlpatterns = [
    path("home/", NotificationListView.as_view(), name="notification_home"),
    path("add/", NotificationCreateView.as_view(), name="create_notification"),
    path("update/<pk>", NotificationUpdateView.as_view(), name="update_notification"),
    path("delete/<pk>", NotificationDeleteView.as_view(), name="delete_notification"),
]
