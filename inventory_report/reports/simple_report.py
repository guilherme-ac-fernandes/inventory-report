from collections import Counter
from datetime import datetime


class SimpleReport:
    @staticmethod
    def generate(list: list):

        today_date = datetime.now().strftime('%Y-%m-%d')

        oldest_date = min([item["data_de_fabricacao"] for item in list])

        closest_date = min(([item["data_de_validade"]
                            for item in list
                            if item["data_de_validade"] > today_date]))

        company_bigger_stock, _ = Counter([item["nome_da_empresa"]
                                           for item in list]).most_common()[0]
        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {closest_date}\n"
            f"Empresa com mais produtos: {company_bigger_stock}"
        )
