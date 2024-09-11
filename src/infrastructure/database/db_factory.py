from src.core.interfaces.db_connection_interface import DBConnectionInterface
from .firebird_connection import FirebirdConnection


class DBFactory:
    @staticmethod
    def get_connection(
        db_type: str, connection_string: str, user: str, password: str
    ) -> DBConnectionInterface:
        if db_type == "firebird":
            return FirebirdConnection(connection_string, user, password)
        else:
            raise ValueError(f"Tipo de base de datos {db_type} no soportado")
