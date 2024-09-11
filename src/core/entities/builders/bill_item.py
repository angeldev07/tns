from __future__ import annotations
from abc import ABC, abstractmethod
from src.core.entities import BillItem


class IBillItemBuilder(ABC):

    @abstractmethod
    def build(self) -> BillItem:
        pass

    @abstractmethod
    def id(self) -> IBillItemBuilder:
        pass

    @abstractmethod
    def description(self) -> IBillItemBuilder:
        pass

    @abstractmethod
    def base_value(self) -> IBillItemBuilder:
        pass


class BillItemBuilder(IBillItemBuilder):

    def __init__(self) -> None:
        self.__reset__()

    def __reset__(self):
        self._bill_item = BillItem()

    def id(self, id) -> IBillItemBuilder:
        self._bill_item.id = id
        return self

    def description(self, description: str) -> IBillItemBuilder:
        self._bill_item.description = description
        return self

    def base_value(self, value: float) -> IBillItemBuilder:
        self._bill_item.base_value = value
        return self

    def build(self) -> BillItem:
        obj = self._bill_item
        self.__reset__()
        return obj
