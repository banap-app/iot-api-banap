from abc import ABC,abstractmethod
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class DataRepository(ABC):
    @abstractmethod
    def add(self, data_of_persistent):
        raise NotImplementedError("add is not implemented")