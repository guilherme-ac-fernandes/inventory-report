from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        with open(path, encoding="utf-8") as file:
            inventory = csv.DictReader(file, delimiter=",", quotechar='"')
            return list(inventory)
