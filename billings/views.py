from django.views.generic import TemplateView

from dashboard.utils.today_money import TodayMoney


class BillingView(TemplateView):
    template_name = "billings/billing_home_page.html"

    def get_context_data(self, **kwargs):
        today_profit = TodayMoney(self.request.user)
        context = {
            "today_profit": today_profit.today_profit,
        }
        return context
