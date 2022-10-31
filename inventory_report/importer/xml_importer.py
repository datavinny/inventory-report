from inventory_report.importer.importer import Importer
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if not path.endswith("xml"):
            raise Exception("Arquivo inválido")
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
            reports = xmltodict.parse(file.read())["dataset"]["record"]
            # reports = result_xml["dataset"]["record"]
            if type == "simples":
                return SimpleReport().generate(reports)
            elif type == "completo":
                return CompleteReport().generate(reports)
