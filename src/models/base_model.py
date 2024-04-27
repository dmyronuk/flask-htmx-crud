from abc import ABC, abstractmethod


class BaseModel(ABC):
    @abstractmethod
    def get_one(self, id: int):
        pass

    @abstractmethod
    def get_many(self, limit=10):
        pass

    @abstractmethod
    def create(self, todo: dict):
        pass

    @abstractmethod
    def update(self, id: int, todo: dict):
        pass

    @abstractmethod
    def delete(self, id: int, todo: dict):
        pass
