from abc import ABC, abstractmethod


class IClassifier(ABC):
    @abstractmethod
    def classify(self, *args, **kwargs):
        raise NotImplementedError()
