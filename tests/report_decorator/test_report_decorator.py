from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


MOCK_LIST = [
    {
        "id": "1",
        "nome_do_produto": "Nicotine Polacrilex",
        "nome_da_empresa": "Target Corporation",
        "data_de_fabricacao": "2021-02-18",
        "data_de_validade": "2023-09-17",
        "numero_de_serie": "CR25 1551 4467 2549 4402 1",
        "instrucoes_de_armazenamento": "instrucao 1",
    },
    {
        "id": "2",
        "nome_do_produto": "NITROUS OXIDE",
        "nome_da_empresa": "Galena Biopharma",
        "data_de_fabricacao": "2020-12-22",
        "data_de_validade": "2024-11-07",
        "numero_de_serie": "CZ09 8588 0858 8435 9140 2695",
        "instrucoes_de_armazenamento": "instrucao 3",
    }
]


def test_decorar_relatorio():
    simple_colored_report = ColoredReport(SimpleReport).generate(MOCK_LIST)
    complete_colored_report = ColoredReport(CompleteReport).generate(MOCK_LIST)

    assert ("\033[31m" in simple_colored_report) is True
    assert ("\033[32m" in simple_colored_report) is True
    assert ("\033[36m" in simple_colored_report) is True

    assert ("\033[31m" in complete_colored_report) is True
    assert ("\033[32m" in complete_colored_report) is True
    assert ("\033[36m" in complete_colored_report) is True
