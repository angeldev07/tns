from abc import ABC, abstractmethod
from core.entities import BillItem


class IBillItemRepository(ABC):

    @abstractmethod
    def get_billItem(self) -> BillItem:
        """Obtiene un unico elemento de la factura.

        Returns:
            BillItem: Objeto de tipo BillItem
        """
        pass

    @abstractmethod
    def get_all_billItems(self) -> list[BillItem]:
        pass
