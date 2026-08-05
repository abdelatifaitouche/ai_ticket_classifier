from abc import ABC, abstractmethod


class IQna(ABC):
    @abstractmethod
    def run(self, *args, **kwargs):
        pass
