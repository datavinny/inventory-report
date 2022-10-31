from collections import Counter
from inventory_report.utils import nearest
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def __filterData(cls, reports):
        oldest_date = "3000-12-31"
        companies = []
        date_list = []
        for report in reports:
            if (report["nome_da_empresa"]):
                companies.append(report["nome_da_empresa"])
            if (report["data_de_validade"]):
                date_list.append(report["data_de_validade"])
            if (report["data_de_fabricacao"] < oldest_date):
                oldest_date = report["data_de_fabricacao"]
        closest_date = nearest(date_list)
        company_bigger_stock = Counter(companies).most_common(1)[0][0]
        return (
          {"companies": companies,
           "oldest_date": oldest_date,
           "closest_date": closest_date,
           "company_bigger_stock": company_bigger_stock}
        )

    @classmethod
    def generate(cls, reports):
        result = cls.__filterData(reports)
        oldest_date = result["oldest_date"]
        closest_date = result["closest_date"]
        company_bigger_stock = result["company_bigger_stock"]
        companies = result["companies"]
        companies_and_products = []
        company_name = ""
        quantity = ""
        for element in Counter(companies):
            print(element)
            if (type(element) == str):
                company_name = element
            elif (type(element) == int):
                quantity = element
            companies_and_products.append(f"{company_name}: {quantity}\n")
        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {closest_date}\n"
            f"Empresa com mais produtos: {company_bigger_stock}\n"
            f"Produtos estocados por empresa:\n"
        )
