from django.urls import path

from .views import (
    CategoryCreateView,
    CategoryDeleteView,
    CategoryListView,
    CategoryUpdateView,
)

urlpatterns = [
    path("home/", CategoryListView.as_view(), name="category-home"),
    path("add/", CategoryCreateView.as_view(), name="create_category"),
    path("update/<pk>", CategoryUpdateView.as_view(), name="update_category"),
    path("delete/<pk>", CategoryDeleteView.as_view(), name="delete_category"),
]
