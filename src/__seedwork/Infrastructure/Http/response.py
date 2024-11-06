from abc import ABC, abstractmethod
from typing import Any
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class IResponse(ABC):
    @abstractmethod
    def set_data(self, data: Any) -> None:
        """Interface para configurar os dados da resposta"""
        pass

    @abstractmethod
    def get_data(self) -> Any:
        """Interface para retornar os dados da resposta"""
        pass