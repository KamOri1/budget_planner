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
    path("wallets/", include("wallet.urls")),
    path("accounts/", include("bank_account.urls")),
    path("categorys/", include("category.urls")),  # <- categories
    path("transactions/", include("transaction.urls")),
    path("goals/", include("saving_goal.urls")),
    path("expenses/", include("regular_expenses.urls")),
    path("possessions/", include("possession_status.urls")),
    path("notifications/", include("notifications.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
