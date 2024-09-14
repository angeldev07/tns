# firebird_connection.py
import fdb
from src.core.interfaces.db_connection_interface import DBConnectionInterface


class FirebirdConnection(DBConnectionInterface):
    def __init__(self, connection_string: str, user: str, password: str):
        self.connection_string = connection_string
        self.user = user
        self.password = password
        self.connection = None

    def connect(self):
        self.connection = fdb.connect(
            dsn=self.connection_string,
            user=self.user,
            password=self.password,
        )

    def execute_query(self, query: str, params: tuple = ()):
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()

    def execute_query_map(self, query: str, params: tuple = ()):
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        return cursor.itermap()

    def close(self):
        if self.connection:
            self.connection.close()
