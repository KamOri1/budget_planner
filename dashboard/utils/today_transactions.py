from datetime import datetime

from django.contrib.auth.models import User
from django.db.models import QuerySet

from category.models import Category
from transaction.models import Transaction


class TodayTransactions:
    def __init__(self, user: "User" = None):
        self.today = datetime.now()
        self.category: QuerySet = Category.objects.filter(user_id=user)
        self.transactions: QuerySet = Transaction.objects.filter(user_id=user)
        self.transaction_list: list = []

    def daily_transactions(self) -> list:

        for transaction in self.transactions:
            if transaction.transaction_date.strftime(
                "%Y-%m-%d"
            ) == datetime.now().strftime("%Y-%m-%d"):
                for transaction_item in self.transaction_list:
                    if transaction_item["name"] == transaction.transaction_name:
                        transaction_item["value"] += transaction.sum_amount

                if str(transaction.category.type) == "profit":
                    category_type = "profit"
                else:
                    category_type = "cost"
                self.transaction_list.append(
                    {
                        "name": transaction.transaction_name,
                        "value": transaction.sum_amount,
                        "type": category_type,
                    }
                )
        if not self.transaction_list:
            self.transaction_list = [
                {"name": "No transaction to view", "value": 0, "type": "profit"}
            ]

        return self.transaction_list

    def transaction_color(self):
        color_dict: dict = {}
        for item in self.transaction_list:
            if item["type"] == "profit":
                color_dict[item["name"]] = "#4CAF50"
            else:
                color_dict[item["name"]] = "#F44335"

        return color_dict
