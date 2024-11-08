from typing import Any, Dict
from ....__seedwork.Infrastructure.Http.request import IRequest

class SimpleRequest(IRequest):
    """
    Implementação simples da interface IRequest, que armazena os dados de uma requisição.
    """
    
    def __init__(self, data: Dict[str, Any]):
        """
        Inicializa o SimpleRequest com os dados da requisição.
        :param data: Dicionário contendo os dados da requisição.
        """
        self._data = data

    def get_data(self) -> Dict[str, Any]:
        """
        Retorna os dados da requisição.
        :return: Dicionário com os dados.
        """
        return self._data
