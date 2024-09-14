from typing import Any
from abc import ABC, abstractmethod
import requests
from src.core.entities import Bill


class IBillSenderService(ABC):

    @abstractmethod
    def send_bills(data: any, endpoint: str) -> None:
        pass

    @abstractmethod
    def send_bill(bill: Bill, endpoint: str) -> None:
        pass


class BillSenderService(IBillSenderService):

    def send_bills(data: Any, endpoint: str) -> None:
        res = requests.post(url=endpoint, data=data)

        if res.status_code != 200:
            raise Exception("Ha fallado el envío de las facturas. Intentelo mas tarde.")

    def send_bill(bill: Bill, endpoint: str) -> None:
        res = requests.post(url=endpoint, data={"bill": bill.to_json()})

        if res.status_code != 200:
            raise Exception("Ha fallado el envío de la factura. Intentelo mas tarde.")
