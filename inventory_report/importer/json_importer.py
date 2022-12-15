from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        with open(path, mode="r") as file:
            inventory = json.load(file)
            return inventory
