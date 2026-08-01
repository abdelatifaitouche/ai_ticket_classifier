from abc import ABC, abstractmethod


class IRepository(ABC):
    @abstractmethod
    def save(self, *args, **kwargs):
        raise NotImplementedError()

    @abstractmethod
    def get_by_id(self, *args, **kwargs):
        raise NotImplementedError()

    @abstractmethod
    def delete(self, *args, **kwargs):
        raise NotImplementedError()

    @abstractmethod
    def update(self, *args, **kwargs):
        raise NotImplementedError()
