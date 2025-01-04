from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from dashboard.views import billing, dashboard, main_view, notifications

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", main_view, name="home_page"),
    path("dashboard", dashboard, name="dashboard"),
    path("billing", billing, name="billing"),
    path("notifications", notifications, name="notifications"),
    path("users/", include("users.urls")),
    path("wallet/", include("wallet.urls")),
    path("account/", include("bank_account.urls")),
    path("category/", include("category.urls")),
    path("transaction/", include("transaction.urls")),
    path("goal/", include("saving_goal.urls")),
    path("expenses/", include("regular_expenses.urls")),
    path("possessions/", include("possession_status.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
