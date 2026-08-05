from abc import ABC, abstractmethod


class IGrader(ABC):
    @abstractmethod
    def run(self, *args, **kwargs):
        raise NotImplementedError()
