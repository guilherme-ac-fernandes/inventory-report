from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        with open(path) as file:
            inventory = xmltodict.parse(file.read())['dataset']['record']
            return inventory
