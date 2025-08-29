from django.views.generic import TemplateView

from datetime import date
from datetime import timedelta

from dashboard.utils.today_money import TodayMoney
from transaction.models import Transaction

from .utils.possesion_values import PossessionValues


class BillingView(TemplateView):
    template_name = "billings/billing_home_page.html"

    def get_context_data(self, **kwargs):
        today_profit = TodayMoney(self.request.user)
        today = date.today()
        yesterday = today - timedelta(days=1)
        context = {
            "today_profit": today_profit.today_profit,
            "possession_values": PossessionValues(self.request.user).calculate(),
            "transactions_today": Transaction.objects.filter(transaction_date__date=today),
            "transactions_yesterday": Transaction.objects.filter(transaction_date__date=yesterday),
        }
        print(context)
        return context


# TODO dodać  context celu oszczędzania, statusu posiadania, regularnych wydatkoów, ostatnie 3 transakcje
