# repositories/factura_repository.py
from abc import ABC, abstractmethod
from src.core.entities.bill import Bill
from src.core.entities.bill_item import BillItem


class IBillRepository(ABC):
    # @abstractmethod
    # def get_bill(self, numero_factura: int) -> Bill:
    #     """Obtiene una factura desde la base de datos usando su número."""
    #     pass

    @abstractmethod
    def get_all_bills_by_period(self, period: int) -> list[Bill]:
        pass

    # @abstractmethod
    # def get_billItem(self) -> BillItem:
    #     """Obtiene un unico elemento de la factura.

    #     Returns:
    #         BillItem: Objeto de tipo BillItem
    #     """
    #     pass

    # @abstractmethod
    # def get_all_billItems(self) -> list[BillItem]:
    #     pass
