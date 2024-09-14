from src.core.interfaces import IUnitsRepository
from src.core.entities import Client
from typing import List, Any


class GetUnitsUseCase:

    def __init__(self, unitRepository: IUnitsRepository):
        self.unitRepository = unitRepository

    def get_unitis(self) -> List[Client]:
        return self.unitRepository.get_all_units()
