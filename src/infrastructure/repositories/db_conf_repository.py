from src.core.interfaces import IDatabBaseConfRepository, DBConnectionInterface
from typing import List


class DatabaseConfImpl(IDatabBaseConfRepository):

    def __init__(self, db_connection: DBConnectionInterface):
        self.db_connection = db_connection

    def get_all_tables(self) -> List[str]:
        self.db_connection.connect()
        query = """
            SELECT a.RDB$RELATION_NAME as name
            FROM RDB$RELATIONS a
            WHERE COALESCE(RDB$SYSTEM_FLAG, 0) = 0 AND RDB$RELATION_TYPE = 0
        """
        res = self.db_connection.execute_query(query=query)
        self.db_connection.close()
        return sorted(list(map(lambda x: x[0].strip(), res)))

    def get_values(self, table: str):
        self.db_connection.connect()
        query = """"""

    def get_cols_by_table(self, table: str) -> List[str]:
        self.db_connection.connect()
        query = f"""
            SELECT 
                rf.RDB$FIELD_NAME AS COLUMN_NAME
            FROM 
                RDB$RELATION_FIELDS rf
            JOIN 
                RDB$FIELDS f ON rf.RDB$FIELD_SOURCE = f.RDB$FIELD_NAME
            WHERE 
                rf.RDB$RELATION_NAME = ?
            ORDER BY 
                rf.RDB$FIELD_POSITION;
        """
        res = self.db_connection.execute_query(query=query, params=(table.upper(),))
        return list(map(lambda x: x[0].strip(), res))
