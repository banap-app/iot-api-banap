from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TypeVar, Generic

T = TypeVar('T')

@dataclass(frozen=True, slots=True)
class Nullary(ABC):
    @abstractmethod
    def execute() -> T:
        raise NotImplementedError("execute() is not implemented")