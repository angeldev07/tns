from ..entities.client import Client
from ..entities.bill_item import BillItem


from typing import List
from datetime import datetime


class Bill:
    """
    Clase que modela la factura
    """

    def __init__(self) -> None:
        self.date: datetime = None  # fecha de la factura
        self.period: int = None
        self.exp_days: int = None
        self.expiration_date: datetime = None
        self.client: Client = None
        self.items: List[BillItem] = []
        self.total: float = 0.0
        self.bill_number: str = ""

    def add_item(self, item: BillItem) -> None:
        self.items.append(item)
        self.__sum_item_value__(item.base_value)  # TODO: Cambiar esta implementación

    def calc_total(self):
        for value in self.items:
            self.total += value.base_value

    def builder():
        from src.core.entities.builders import BillBuilder

        return BillBuilder()

    def __sum_item_value__(self, value: float) -> None:
        self.total += value

    def __str__(self) -> str:
        items_str = (
            "\n".join([str(item) for item in self.items]) if self.items else "No items"
        )
        return (
            f"Bill: {self.bill_number} \n"
            f" - Date: {self.date}\n"
            f" - Period: {self.period}\n"
            f" - Expiration Days: {self.exp_days}\n"
            f" - Expiration Date: {self.expiration_date}\n"
            f" - Client: {self.client}\n"
            f" - Items:\n{items_str}\n"
            f" - Total: {self.total:.2f}\n"
        )
