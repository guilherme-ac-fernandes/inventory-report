# Projeto Inventory Report 📑📈

Consiste em uma aplicação para geração de relatórios que recebe como entrada arquivos com dados de um estoque e gera, como saída, um relatório acerca destes dados. A aplicação tem suporte para arquivos nos formatos: `JSON`, `CSV` e `XML`.

* Construído utilizando Python, princípios da Programação Orientada a Objetos e Padrões de Projetos

<br />

<details>
  <summary><strong>Descrição das classes criadas:</strong></summary><br />

| Classe | Descrição | Localização |
|---|---|---|
| `simple_report` | Classe para gerar a versão simplificada do relatório | `inventory_report/reports/simple_report.py` |
| `complete_report` | Classe para gerar a versão completa do relatório | `inventory_report/reports/complete_report.py` |
| `inventory` | Classe para gerar os relatório a partir de arquivos | `inventory_report/inventory/inventory.py` |
| `importer` | Classe abstrata para aplicar o padrão de projeto `Strategy` | `inventory_report/importer/importer.py` |
| `inventory_iterator` | Refatoração da classe `Inventory` para aplicar o padrão de projeto `Iterator` | `inventory_report/inventory/inventory_iterator.py` |

<br />
</details>

<details>
  <summary><strong>Descrição dos testes criados:</strong></summary><br />
 
| Teste | Descrição | Localização |
|---|---|---|
| `test_product` | Implementação dos testes para a classe `Product` | `tests/product/test_product.py` |
| `test_product_report` | Implementação dos testes para a  a criação do relatório presente na classe `Product` | `tests/product_report/test_product_report.py` |
| `test_report_decorator` | Implementação dos testes para a classe `ColoredReport` | `tests/report_decorator/test_report_decorator.py` |

<br />
</details>


### Estrutura do Projeto

```
.
├── inventory_report
│   ├── data
│   │   ├── 🔸inventory.csv
│   │   ├── 🔸inventory.json
│   │   └── 🔸inventory.xml
│   ├── importer
│   │   ├── 🔹csv_importer.py
│   │   ├── 🔹importer.py
│   │   ├── 🔹json_importer.py
│   │   └── 🔹xml_importer.py
│   ├── inventory
│   │   ├── 🔹inventory_iterator.py
│   │   ├── 🔹inventory_refactor.py
│   │   └── 🔹inventory.py
│   │   └── 🔸product.py
│   ├── reports
│   │   ├── 🔸colored_report.py
│   │   ├── 🔹complete_report.py
│   │   └── 🔹simple_report.py
│   └── 🔹main.py
└── tests
│   ├── factories
│   │   ├── 🔸__init__.py
│   │   └── 🔸product_factory.py
│   ├── product
│   │   ├── 🔸__init__.py
│   │   └── 🔹test_product.py
│   ├── product_report
│   │   ├── 🔸__init__.py
│   │   └── 🔹test_product_report.py
│   ├── report_decorator
│   │   ├── 🔸__init__.py
│   │   └── 🔹test_report_decorator.py
│   └── 🔸__init__.py
├── 🔹dev-requirements.txt
├── 🔸docker-compose.yml
├── 🔸Dockerfile
├── 🔸pyproject.toml
├── 🔸README.md
├── 🔸requirements.txt
├── 🔸setup.cfg
└── 🔸setup.py

Legenda:
🔸 Arquivos desenvolvidos pela Trybe (não foram alterados).
🔹 Arquivos desenvolvidos por mim.

```


### Instruções

- Para rodar a aplicação localmente e os testes, realize o clone do projeto e utilize os comandos a seguir:

```
Para instalar as dependências e iniciar as aplicações:
<-- na raiz do projeto -->
python3 -m venv .venv // para criar o ambiente virtual
source .venv/bin/activate // para ativar o ambiente virtual
python3 -m pip install -r dev-requirements.txt // instalação das dependências

Para gerar os relatórios via linha de comando:
<-- na raiz do projeto -->
pip install . // para instalar a dependência da linha de comando
inventory_report <argumento1> <argumento2>
--> <argumento1> = deve receber o caminho de um arquivo a ser importado
--> <argumento2> = formato do relatório (simples ou completo)
ou
python3 -m inventory_report.main <argumento1> <argumento2>

Para rodar todos os testes:
<-- na raiz do projeto -->
python3 -m pytest

Para rodar os testes individualmente:
<-- na raiz do projeto -->
python3 -m pytest -k test_cria_produto
python3 -m pytest -k test_relatorio_produto
python3 -m pytest -k test_decorar_relatorio

Para rodar os testes utilizando Docker:
<-- na raiz do projeto -->
docker-compose run --rm inventory pytest
```

### Demonstração

Relatório Simples

> Comando: `python3 -m inventory_report.main ./inventory_report/data/inventory.csv simples`

```
Data de fabricação mais antiga: 2020-09-06
Data de validade mais próxima: 2023-09-17
Empresa com mais produtos: Target Corporation
```

Relatório Completo

> Comando: `python3 -m inventory_report.main ./inventory_report/data/inventory.xml completo`

```
Data de fabricação mais antiga: 2020-09-06
Data de validade mais próxima: 2023-09-17
Empresa com mais produtos: Target Corporation
Produtos estocados por empresa:
- Target Corporation: 4
- Galena Biopharma: 2
- Cantrell Drug Company: 2
- Moore Medical LLC: 1
- REMEDYREPACK: 1
```

