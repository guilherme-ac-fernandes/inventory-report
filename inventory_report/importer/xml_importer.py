from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    @classmethod
    def import_data(self, path):
        if 'xml' not in path:
            raise ValueError('Arquivo inválido')
        with open(path) as file:
            inventory = xmltodict.parse(file.read())['dataset']['record']
            return inventory
