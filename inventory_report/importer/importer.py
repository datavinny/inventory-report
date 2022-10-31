from abc import ABC, abstractmethod


class Importer(ABC):  # Interface
    @classmethod
    @abstractmethod
    def import_data(cls, path):
        raise NotImplementedError
