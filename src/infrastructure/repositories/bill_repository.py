from typing import List, Dict
from src.core.interfaces.bill_respository_interface import IBillRepository
from src.core.entities import Bill, BillItem, Client
from src.core.interfaces.db_connection_interface import DBConnectionInterface


class BillRespositoryImpl(IBillRepository):

    def __init__(self, db_connection: DBConnectionInterface):
        self.db_connection = db_connection

    def get_all_bills_by_period(self, period: int) -> List[Bill]:
        self.db_connection.connect()
        try:
            query = """
                SELECT kx.KARDEXID, kx.FECHA, kx.PERIODO, kx.PLAZODIAS, kx.FECVENCE, t.TERID, t.NITTRI, t.NOMBRE, t.NIT, m.MATID, m.DESCRIP, SUM(dkx.PRECIOBASE), kx.CODPREFIJO || ' ' || kx.NUMERO as numero
                FROM DEKARDEX dkx
                JOIN KARDEX kx on (kx.KARDEXID = dkx.KARDEXID)
                JOIN MATERIAL m on (m.MATID = dkx.MATID)
                JOIN TERCEROS t on (kx.cliente = t.TERID)
                WHERE kx.periodo = ?
                GROUP BY kx.KARDEXID, kx.FECHA, kx.PERIODO, kx.PLAZODIAS, kx.FECVENCE, t.TERID, t.NITTRI, t.NOMBRE, t.NIT, m.MATID, m.DESCRIP, numero
                ORDER BY t.TERID
            """

            # execute the query
            bills = self.db_connection.execute_query(
                query=query, params=(f"0{period}" if period < 10 else f"{period}",)
            )

            return self.__group_by_bill__(bills)

        finally:
            self.db_connection.close()

    def __group_by_bill__(self, bills) -> List[Dict]:
        bill_map: Dict[str, Bill] = {}
        for bill in bills:
            bill_id = bill[0]

            if not bill_id in bill_map:
                client = (
                    Client.builder()
                    .Id(bill[5])
                    .cedula(bill[6])
                    .partial_full_name(bill[7])
                    .residence_id(bill[8])
                    .build()
                )
                item = (
                    BillItem.builder()
                    .id(bill[9])
                    .description(bill[10])
                    .base_value(bill[11])
                    .build()
                )
                bill = (
                    Bill.builder()
                    .date(bill[1])
                    .period(bill[2])
                    .exp_days(int(bill[3]))
                    .expiration_date(bill[4])
                    .client(client)
                    .items([item])
                    .bill_number(bill[12])
                    .build()
                )
                bill_map[bill_id] = bill
            else:
                bill_map[bill_id].add_item(
                    (
                        BillItem.builder()
                        .id(bill[9])
                        .description(bill[10])
                        .base_value(bill[11])
                        .build()
                    )
                )

        return list(bill_map.values())
