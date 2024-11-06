from dataclasses import dataclass
from ...__seedwork.Infrastructure.Http.request import IRequest
@dataclass(frozen=True, slots=True)
class SimpleRequest(IRequest):
    def __init__(self, data: dict):
        self._data = data

    def get_data(self) -> dict:
        return self._data

