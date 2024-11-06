from dataclasses import dataclass
from ...__seedwork.Infrastructure.Http.request import IResponse
@dataclass(frozen=True, slots=True)
class SimpleResponse(IResponse):
    def __init__(self):
        self._data = None

    def set_data(self, data: Any) -> None:
        self._data = data

    def get_data(self) -> Any:
        return self._data