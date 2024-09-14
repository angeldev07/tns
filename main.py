from src.core.use_cases import GetBillsUseCase, ConfCuotaUseCase, GetUnitsUseCase
from src.infrastructure.database.db_factory import DBFactory
from src.infrastructure.repositories import (
    BillRespositoryImpl,
    DatabaseConfImpl,
    UnitsRespositoryImpl,
)
from src.application.view import UnitsView
import json
import os


def gen_bills():
    db = DBFactory.get_connection(
        "firebird", r"localhost:D:\Datos TNS\DEMOTNS2024.GDB", "SYSDBA", "masterkey"
    )

    get_bill_use = GetBillsUseCase(BillRespositoryImpl(db))

    bills = get_bill_use.get_all_bills_by_period(1)

    for bill in bills:
        print(json.dumps(bill.to_json(), indent=4))


def conf_cuouta():
    db = DBFactory.get_connection(
        "firebird", r"localhost:D:\Datos TNS\DEMOTNS2024.GDB", "SYSDBA", "masterkey"
    )

    tables_use = ConfCuotaUseCase(DatabaseConfImpl(db))

    return tables_use.conf_cuouta()


def units():
    db = DBFactory.get_connection(
        "firebird", r"localhost:D:\Datos TNS\DEMOTNS2024.GDB", "SYSDBA", "masterkey"
    )
    units = GetUnitsUseCase(UnitsRespositoryImpl(db))
    return units.get_unitis()


def continuar_flow():
    res = int(input("¿Desea continuar? \n1.Si.\n2.No.\n"))
    return -1 if res < 1 or res > 2 else res


def main():

    menu = """
1. Configurar Cuota administrativa.
2. Generar facturas.
3. Reportar factura por unidad. 
3. Reportar unidades. 
4. Salir 

opcion: 
    """

    while True:
        option = int(input(menu))

        if option < 1 or option > 4:
            print("Opción no valida.")
            os.system("cls" if os.name == "nt" else "clear")
            continue

        if option == 1:
            res = conf_cuouta()
            print(res)

        if option == 2:
            gen_bills()

        if option == 3:
            UnitsView(units())

            # for unit in res:
            #     print(json.dumps(unit.to_json(), indent=4))

        if option == 4:
            break

        break

        flow = continuar_flow()
        if flow == -1 or flow == 2:
            break


if __name__ == "__main__":
    main()
