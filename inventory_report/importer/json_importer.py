from inventory_report.importer.importer import Importer
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if not path.endswith("json"):
            raise ValueError("Arquivo inválido")
        """Reads a file from a given path and returns its contents
        Parameters
        ----------
        path : str
            Full path to file
        Returns
        -------
        list
            List of rows as dicts
        """
        with open(path, encoding="utf-8") as file:
            reports = json.load(file)
            if type == "simples":
                return SimpleReport().generate(reports)
            elif type == "completo":
                return CompleteReport().generate(reports)
