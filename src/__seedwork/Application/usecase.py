from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class UseCase(ABC):
    @abstractmethod
    def execute():
        raise NotImplementedError("execute() is not implemented")