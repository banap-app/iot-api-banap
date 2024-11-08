from typing import Any, Dict
from dataclasses import dataclass
from ....__seedwork.Infrastructure.Http.response import IResponse


@dataclass
class SimpleResponse(IResponse):
    data: Dict[str, Any] = None

    def set_data(self, data: Dict[str, Any]) -> None:
        """Configura os dados da resposta."""
        self.data = data

    def get_data(self) -> Dict[str, Any]:
        """Retorna os dados da resposta."""
        return self.data

    def is_success(self) -> bool:
        """Verifica se a resposta indica sucesso."""
        return self.data.get("success", False)
