from abc import ABC, abstractmethod
from typing import List, Any
from src.core.entities import Client


class IUnitsRepository(ABC):

    @abstractmethod
    def get_all_units(self) -> List[Client]:
        pass

    @abstractmethod
    def get_unit_by_id(self, id: str) -> Client:
        pass
