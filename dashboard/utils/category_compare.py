from datetime import datetime

from django.db.models import QuerySet

from category.models import Category
from transaction.models import Transaction


class CategoryCompare:
    def __init__(self):
        self.today = datetime.now()
        self.category: QuerySet = Category.objects.all()
        self.transactions: QuerySet = Transaction.objects.all()
        self.category_values_list: list = []

    def compare_category_values(self):
        current_month = datetime.now().strftime("%Y-%m")

        for transaction in self.transactions:
            if transaction.transaction_date.strftime("%Y-%m") == current_month:
                found = False

                for category_item in self.category_values_list:
                    if category_item["name"] == transaction.category_id:
                        category_item["value"] += transaction.sum_amount
                        found = True
                        break

                if not found:
                    name = transaction.category_id.category_name
                    self.category_values_list.append(
                        {
                            "name": name,
                            "value": transaction.sum_amount,
                        }
                    )

        if not self.category_values_list:
            self.category_values_list = [{"name": "No category to view", "value": 0}]
        print(self.category_values_list)
        return self.category_values_list
