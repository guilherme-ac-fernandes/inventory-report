from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(list: list):

        simple_report = SimpleReport.generate(list)

        company_stock = {}
        for item in list:
            if item["nome_da_empresa"] in company_stock:
                company_stock[item["nome_da_empresa"]] += 1
            else:
                company_stock[item["nome_da_empresa"]] = 1

        # Utilização do .items em dict proveniente do Stack OverFlow
        # source: https://stackoverflow.com/questions/3294889/iterati
        # ng-over-dictionaries-using-for-loops
        company_amount_list = ""
        for key, value in company_stock.items():
            company_amount_list += f"- {key}: {value}\n"

        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{company_amount_list}"
        )

