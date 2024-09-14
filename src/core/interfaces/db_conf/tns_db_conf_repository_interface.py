from abc import ABC, abstractmethod
from typing import List


class IDatabBaseConfRepository(ABC):

    @abstractmethod
    def get_all_tables(self) -> List[str]:
        pass

    @abstractmethod
    def get_cols_by_table(self, table: str) -> List[str]:
        pass

    @abstractmethod
    def get_values(self, table: str):
        pass
