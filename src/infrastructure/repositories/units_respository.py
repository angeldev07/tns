from src.core.interfaces import IUnitsRepository
from src.core.interfaces import DBConnectionInterface
from src.core.entities import Client
from typing import List, Any


class UnitsRespositoryImpl(IUnitsRepository):

    def __init__(self, db: DBConnectionInterface) -> None:
        self.db = db

    def get_all_units(self) -> List[Client]:
        self.db.connect()
        query = """
            SELECT TERID, NITTRI, NIT, NOMBRE
            FROM TERCEROS 
        """
        res = self.db.execute_query(query=query)

        return list(map(self.__map_to_client__, res))

    def get_unit_by_id(self, id: str) -> Client:
        pass

    def __map_to_client__(self, client: tuple) -> Client:
        return (
            Client.builder()
            .Id(client[0])
            .cedula(client[1])
            .residence_id(client[2])
            .partial_full_name(client[3])
            .build(),
        )[0]
