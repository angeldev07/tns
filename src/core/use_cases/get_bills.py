from src.core.interfaces.bill_respository_interface import IBillRepository
from typing import List
from src.core.entities.bill import Bill


class GetBillsUseCase:

    def __init__(self, billRespository: IBillRepository):
        self.billRespository = billRespository

    def get_all_bills_by_period(self, period: int) -> List[Bill]:

        if period < 0 or period > 12:
            raise ValueError("Period invalid. Please, select a period between 1 and 12")

        return self.billRespository.get_all_bills_by_period(period)
