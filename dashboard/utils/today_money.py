from datetime import datetime, timedelta

from django.db.models import QuerySet

from category.models import Category
from transaction.models import Transaction


class TodayMoney:
    def __init__(self):
        self.category: QuerySet = Category.objects.all()
        self.transactions: QuerySet = Transaction.objects.all()
        self.today_profit: float = self.sum_of_profit() - self.sum_of_expenses()

    def sum_of_profit(self) -> float:
        month_profit: float = 0

        for transaction in self.transactions:
            if transaction.category_id in self.category.filter(category_type="profit"):
                if transaction.transaction_date.strftime(
                    "%Y-%m"
                ) == datetime.now().strftime("%Y-%m"):
                    month_profit += transaction.sum_amount

        return month_profit

    def sum_of_expenses(self) -> float:
        month_expenses: float = 0

        for transaction in self.transactions:
            if transaction.category_id in self.category.filter(category_type="cost"):
                if transaction.transaction_date.strftime(
                    "%Y-%m"
                ) == datetime.now().strftime("%Y-%m"):
                    month_expenses += transaction.sum_amount

        return month_expenses

    def compare_monthly_profit(self) -> float:
        current_month_profit = self.sum_of_profit()
        previous_month = datetime.now() - timedelta(days=30)
        previous_month_str = previous_month.strftime("%Y-%m")

        previous_month_profit = 0
        for transaction in self.transactions:
            if transaction.category_id in self.category.filter(category_type="profit"):
                if transaction.transaction_date.strftime("%Y-%m") == previous_month_str:
                    previous_month_profit += transaction.sum_amount

        if previous_month_profit == 0:
            return 0
        else:
            profit_percentage_change = (
                (current_month_profit - previous_month_profit) / previous_month_profit
            ) * 100
            return round(profit_percentage_change)
