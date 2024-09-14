from src.core.interfaces import IDatabBaseConfRepository
from src.application.view import run
from typing import List


class ConfCuotaUseCase:
    def __init__(self, db_conf: IDatabBaseConfRepository):
        self.db_conf = db_conf

    def conf_cuouta(self) -> List[str]:
        tables = self.db_conf.get_all_tables()
        col = run(tables)[1]
        return self.db_conf.get_cols_by_table(col)
