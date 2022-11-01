from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if not path.endswith("xml"):
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
            return xmltodict.parse(file.read())["dataset"]["record"]
