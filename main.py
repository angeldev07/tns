from src.core.use_cases.get_bills import GetBillsUseCase
from src.infrastructure.database.db_factory import DBFactory
from src.infrastructure.repositories.bill_repository import BillRespositoryImpl


def main():
    db = DBFactory.get_connection(
        "firebird", r"localhost:D:\Datos TNS\DEMOTNS2024.GDB", "SYSDBA", "masterkey"
    )

    get_bill_use = GetBillsUseCase(BillRespositoryImpl(db))

    bills = get_bill_use.get_all_bills_by_period(1)

    for bill in bills:
        print(bill, "--------------------------------------------------------------\n")


if __name__ == "__main__":
    main()
