from abc import ABC,abstractmethod
from ...Domain.entities import DataOfEsp
from dataclasses import dataclass
from typing import List
from datetime import datetime

@dataclass(frozen=True, slots=True)
class DataRepository(ABC):
    @abstractmethod
    def add(self, data:DataOfEsp ):
        raise NotImplementedError("add is not implemented")
    
    @abstractmethod
    def get_all(self) -> List[DataOfEsp]:
        raise NotImplementedError("get_all is not implemented")
    
    @abstractmethod
    def get_by_date(self, initialDate: datetime, finalDate: datetime)->List[DataOfEsp]:
        raise NotImplementedError("get_by_date is not implemented")