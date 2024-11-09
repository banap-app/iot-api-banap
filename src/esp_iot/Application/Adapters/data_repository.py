from abc import ABC,abstractmethod
from ...Domain.entities import DataOfEsp
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class DataRepository(ABC):
    @abstractmethod
    def add(self, data:DataOfEsp ):
        raise NotImplementedError("add is not implemented")