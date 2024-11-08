from abc import ABC, abstractmethod
from typing import Any, Dict


class IResponse(ABC):
    """
    Interface para gerenciar as respostas HTTP em controllers, fornecendo 
    métodos para configurar e obter dados de resposta de forma padronizada.
    """
    
    @abstractmethod
    def set_data(self, data: Dict[str, Any]) -> None:
        """Configura os dados da resposta."""
        pass

    @abstractmethod
    def get_data(self) -> Dict[str, Any]:
        """Retorna os dados da resposta no formato de um dicionário."""
        pass

    @abstractmethod
    def is_success(self) -> bool:
        """Verifica se a resposta indica sucesso."""
        pass
