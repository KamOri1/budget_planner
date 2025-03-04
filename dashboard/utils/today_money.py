from datetime import datetime

from django.contrib.auth.models import User
from django.db.models import QuerySet

from category.models import Category
from transaction.models import Transaction


class TodayMoney:
    def __init__(self, user: "User" = None):
        self.category: QuerySet = Category.objects.filter(user_id=user)
        self.transactions: QuerySet = Transaction.objects.filter(user_id=user)
        self.today_profit: float = self.sum_of_profit() - self.sum_of_expenses()

    def sum_of_profit(self) -> float:
        month_profit: float = 0

        for transaction in self.transactions:
            if transaction.category_id in self.category.filter(category_type="2"):
                if transaction.transaction_date.strftime(
                    "%Y-%m"
                ) == datetime.now().strftime("%Y-%m"):
                    month_profit += transaction.sum_amount

        return month_profit

    def sum_of_expenses(self) -> float:
        month_expenses: float = 0

        for transaction in self.transactions:
            if transaction.category_id in self.category.filter(category_type="1"):
                print(self.category)
                if transaction.transaction_date.strftime(
                    "%Y-%m"
                ) == datetime.now().strftime("%Y-%m"):
                    month_expenses += transaction.sum_amount

        return month_expenses

    def compare_monthly_profit(self) -> float:
        current_month_profit: float = self.sum_of_profit()
        previous_month_profit: float = 0
        current_month = datetime.now().strftime("%m")
        current_years = datetime.now().strftime("%Y")

        if int(current_month) == 1:
            previous_month: str = f"{str(int(current_years) - 1)}-12"

        else:
            previous_month: str = f"{current_years}-{str(int(current_month) - 1)}"

        previous_month: datetime = datetime.strptime(previous_month, "%Y-%m")

        for transaction in self.transactions:
            if transaction.category_id in self.category.filter(category_type="2"):
                if transaction.transaction_date.strftime(
                    "%Y-%m"
                ) == previous_month.strftime("%Y-%m"):
                    previous_month_profit += transaction.sum_amount

        if previous_month_profit == 0:
            return 0
        else:
            profit_percentage_change = (
                (current_month_profit - previous_month_profit) / previous_month_profit
            ) * 100
            return round(profit_percentage_change)

    def compare_monthly_expenses(self) -> float:
        current_month_expenses: float = self.sum_of_expenses()
        previous_month_expenses: float = 0
        current_month = datetime.now().strftime("%m")
        current_years = datetime.now().strftime("%Y")

        if int(current_month) == 1:
            previous_month: str = f"{str(int(current_years) - 1)}-12"

        else:
            previous_month: str = f"{current_years}-{str(int(current_month) - 1)}"

        previous_month: datetime = datetime.strptime(previous_month, "%Y-%m")

        for transaction in self.transactions:
            if transaction.category_id in self.category.filter(category_type="1"):
                if transaction.transaction_date.strftime(
                    "%Y-%m"
                ) == previous_month.strftime("%Y-%m"):
                    previous_month_expenses += transaction.sum_amount

        if previous_month_expenses == 0:
            return 0
        else:
            expenses_percentage_change = (
                (current_month_expenses - previous_month_expenses)
                / previous_month_expenses
            ) * 100
            return round(expenses_percentage_change)

    def compare_today_profit(self) -> float:
        current_month_today_profit: float = self.sum_of_profit()
        previous_month_today_profit: float = 0
        current_month = datetime.now().strftime("%m")
        current_years = datetime.now().strftime("%Y")

        if int(current_month) == 1:
            previous_month: str = f"{str(int(current_years) - 1)}-12"

        else:
            previous_month: str = f"{current_years}-{str(int(current_month) - 1)}"

        previous_month: datetime = datetime.strptime(previous_month, "%Y-%m")

        for transaction in self.transactions:
            if transaction.category_id in self.category.filter(category_type="2"):
                if transaction.transaction_date.strftime(
                    "%Y-%m"
                ) == previous_month.strftime(
                    "%Y-%m"
                ) and transaction.transaction_date.strftime(
                    "%d"
                ) <= datetime.now().strftime(
                    "%d"
                ):
                    previous_month_today_profit += transaction.sum_amount

        if previous_month_today_profit == 0:
            return 0
        else:
            profit_percentage_change = (
                (current_month_today_profit - previous_month_today_profit)
                / previous_month_today_profit
            ) * 100
            return round(profit_percentage_change)
