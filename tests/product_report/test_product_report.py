from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product_list = [
        'Alexa',
        'Amazon',
        '12/12/2005',
        'undefined',
        'armazenar em local seco',
    ]

    product = Product(
        id=1,
        nome_do_produto=product_list[0],
        nome_da_empresa=product_list[1],
        data_de_fabricacao=product_list[2],
        data_de_validade=product_list[3],
        numero_de_serie='ALX123456',
        instrucoes_de_armazenamento=product_list[4],
    )

    for string in product_list:
        assert (string in product.__repr__()) is True
