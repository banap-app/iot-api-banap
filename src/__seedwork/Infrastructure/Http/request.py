from abc import ABC, abstractmethod
from typing import Any, Dict


class IRequest(ABC):
    """
    Interface para representar uma requisição e permitir a obtenção dos dados.
    """
    
    @abstractmethod
    def get_data(self) -> Dict[str, Any]:
        """Método abstrato para obter os dados da requisição."""
        pass
