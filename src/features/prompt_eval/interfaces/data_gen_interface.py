from abc import ABC, abstractmethod


class IDataGenerator(ABC):
    @abstractmethod
    def generate(self, *args, **kwargs):
        pass
