from django.urls import path

from users import views as user_views

urlpatterns = [
    # path("register", user_views.register, name="register"),
    path("register/", user_views.RegisterView.as_view(), name="register"),
    path(
        "login/",
        user_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path("logout/", user_views.LogoutView.as_view(), name="logout"),
    path("activate/<uidb64>/<token>", user_views.active, name="activate"),
]
