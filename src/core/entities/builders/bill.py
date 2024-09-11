from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from datetime import datetime
from src.core.entities import Bill, Client, BillItem


class IBillBuilder(ABC):
    """
    Interfaz Abstracta para el BillBuilder.
    """

    @abstractmethod
    def date(self, date: datetime) -> IBillBuilder:
        pass

    @abstractmethod
    def period(self, period: str) -> IBillBuilder:
        pass

    @abstractmethod
    def exp_days(self, exp_days: int) -> IBillBuilder:
        pass

    @abstractmethod
    def expiration_date(self, expiration_date: datetime) -> IBillBuilder:
        pass

    @abstractmethod
    def client(self, client: Client) -> IBillBuilder:
        pass

    @abstractmethod
    def items(self, items: List[BillItem]) -> IBillBuilder:
        pass

    @abstractmethod
    def bill_number(self, bill_number: str) -> IBillBuilder:
        pass

    @abstractmethod
    def build(self) -> Bill:
        pass


class BillBuilder(IBillBuilder):
    """
    Implementación concreta del BillBuilder.
    """

    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self._bill = Bill()

    def date(self, date: datetime) -> BillBuilder:
        self._bill.date = date
        return self

    def period(self, period: str) -> BillBuilder:
        self._bill.period = period
        return self

    def exp_days(self, exp_days: int) -> BillBuilder:
        self._bill.exp_days = exp_days
        return self

    def expiration_date(self, expiration_date: datetime) -> BillBuilder:
        self._bill.expiration_date = expiration_date
        return self

    def client(self, client: Client) -> BillBuilder:
        self._bill.client = client
        return self

    def items(self, items: List[BillItem]) -> BillBuilder:
        self._bill.items = items
        self._bill.calc_total()
        return self

    def bill_number(self, bill_number: str) -> IBillBuilder:
        self._bill.bill_number = bill_number
        return self

    def build(self) -> Bill:
        bill = self._bill
        self.reset()  # Resetea el builder para futuras construcciones
        return bill
