from datetime import datetime

from django.db.models import QuerySet

from category.models import Category
from transaction.models import Transaction


class TodayTransactions:
    def __init__(self):
        self.today = datetime.now()
        self.category: QuerySet = Category.objects.all()
        self.transactions: QuerySet = Transaction.objects.all()
        self.transaction_list: list = []

    def daily_transactions(self) -> list:

        for transaction in self.transactions:

            if transaction.transaction_date.strftime(
                "%Y-%m-%d"
            ) == datetime.now().strftime("%Y-%m-%d"):
                for transaction_item in self.transaction_list:
                    if transaction_item["name"] == transaction.transaction_name:
                        transaction_item["value"] += transaction.sum_amount

                if transaction.category_id in self.category.filter(
                    category_type="cost"
                ):
                    category_type = "cost"
                else:
                    category_type = "profit"
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
