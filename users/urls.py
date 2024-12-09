from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from users import views as user_views

urlpatterns = [
    path("sign-up", user_views.register, name="register"),
    path(
        "login",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path("logout", user_views.logout_user, name="logout"),
]
