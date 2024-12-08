from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from dashboard.views import billing, dashboard, main_view, notifications
from users import views as user_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", main_view),
    path("dashboard", dashboard, name="dashboard"),
    path("billing", billing, name="billing"),
    path("notifications", notifications, name="notifications"),
    path("users/", include("users.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
