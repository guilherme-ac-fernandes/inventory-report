from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xmltodict


class Inventory:
    @staticmethod
    def import_data(path, type):
        if 'csv' in path:
            return Inventory.open_csv(path, type)
        elif 'json' in path:
            return Inventory.open_json(path, type)
        elif 'xml' in path:
            return Inventory.open_xml(path, type)
        else:
            raise ValueError('Invalid format file')

    @staticmethod
    def open_csv(path, type):
        with open(path, encoding="utf-8") as file:
            inventory = csv.DictReader(file, delimiter=",", quotechar='"')
            if type == 'simples':
                return SimpleReport.generate(list(inventory))
            elif type == 'completo':
                return CompleteReport.generate(list(inventory))
            else:
                raise ValueError('Invalid Type')

    @staticmethod
    def open_json(path, type):
        with open(path, mode="r") as file:
            inventory = json.load(file)
            if type == 'simples':
                return SimpleReport.generate(inventory)
            elif type == 'completo':
                return CompleteReport.generate(inventory)
            else:
                raise ValueError('Invalid Type')

    @staticmethod
    def open_xml(path, type):
        # Aplicação da leitura de arquivos XML proveniente do Stack OverFlow
        # source: https://stackoverflow.com/questions/40154727/how-to-use-xml
        # todict-to-get-items-out-of-an-xml-file
        with open(path) as file:
            inventory = xmltodict.parse(file.read())['dataset']['record']
            if type == 'simples':
                return SimpleReport.generate(inventory)
            elif type == 'completo':
                return CompleteReport.generate(inventory)
            else:
                raise ValueError('Invalid Type')
