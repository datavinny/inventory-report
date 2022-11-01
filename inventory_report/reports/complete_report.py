from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, reports):
        products_owners = []
        for report in reports:
            if report["nome_da_empresa"]:
                products_owners.append(report["nome_da_empresa"])
        result = ""
        products_by_company = list(Counter(products_owners).items())
        for item in products_by_company:
            result += f"- {item[0]}: {item[1]}\n"
        return (
            super().generate(reports)
            + "\nProdutos estocados por empresa:\n"
            + result
        )
