from django.views.generic import TemplateView

from dashboard.utils.today_money import TodayMoney

from .utils.possesion_values import PossessionValues


class BillingView(TemplateView):
    template_name = "billings/billing_home_page.html"

    def get_context_data(self, **kwargs):
        today_profit = TodayMoney(self.request.user)
        context = {
            "today_profit": today_profit.today_profit,
            "possession_values": PossessionValues(self.request.user).calculate(),
        }
        print(context)
        return context


# TODO dodać  context celu oszczędzania, statusu posiadania, regularnych wydatkoów, ostatnie 3 transakcje
