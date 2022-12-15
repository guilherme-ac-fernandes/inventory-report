from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


class Inventory:
    @staticmethod
    def import_data(path, type):
        with open(path, encoding="utf-8") as file:
            inventory = csv.DictReader(file, delimiter=",", quotechar='"')
            if type == 'simples':
                return SimpleReport.generate(list(inventory))
            elif type == 'completo':
                return CompleteReport.generate(list(inventory))
            else:
                raise ValueError('Type invalid')
