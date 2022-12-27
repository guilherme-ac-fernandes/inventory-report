from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
import sys


def main():
    if len(sys.argv) <= 3 and (sys.argv[-2] == '' or sys.argv[-1] == ''):
        print(ValueError('Verifique os argumentos'), file=sys.stderr)
        return
    path, type = sys.argv[-2], sys.argv[-1]
    if path.endswith('.csv'):
        print(InventoryRefactor(CsvImporter).import_data(path, type))
        return
    elif path.endswith('.json'):
        print(InventoryRefactor(JsonImporter).import_data(path, type))
        return
    elif path.endswith('.xml'):
        print(InventoryRefactor(XmlImporter).import_data(path, type))
        return
    else:
        raise ValueError('Invalid format file')


# main()

# "Data de fabricação mais antiga: 2020-09-06\n"
# "Data de validade mais próxima: 2023-09-17\n"
# "Empresa com mais produtos: Target Corporation"

# "Data de fabricação mais antiga: 2020-09-06\n"
# "Data de validade mais próxima: 2023-09-17\n"
# "Empresa com mais produtos: Target Corporation"
