from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from dashboard.views import billing, dashboard, main_view, notifications

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", main_view),
    path("dashboard", dashboard, name="dashboard"),
    path("billing", billing, name="billing"),
    path("notifications", notifications, name="notifications"),
    path("users/", include("users.urls")),
    path("", include("wallet.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
