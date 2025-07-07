from django.contrib.auth.models import User
from django.db.models import QuerySet

from possession_status.models import PossessionStatus


class PossessionValues:
    def __init__(self, user: "User" = None):
        self.possession_item: QuerySet = PossessionStatus.objects.filter(user_id=user)

    def calculate(self) -> int:
        item_values: int = 0
        for item in self.possession_item:
            item_values += int(item.asset_value)
        return item_values

    def list(self) -> list[dict]:
        item_list: list[dict] = []
        for item in self.possession_item:
            item_list.append(
                {
                    "asset_name": item.asset_name,
                    "asset_value": item.asset_value,
                    "description": item.description,
                }
            )
        return item_list
