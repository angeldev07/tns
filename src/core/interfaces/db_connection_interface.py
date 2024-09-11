from abc import ABC, abstractmethod


class DBConnectionInterface(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute_query(self, query: str, params: tuple = ()):
        pass

    @abstractmethod
    def close(self):
        pass
