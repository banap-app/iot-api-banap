from ...Domain.entities import DataOfEsp
from ...Application.Adapters.data_repository import DataRepository
from ....__seedwork.Infrastructure.Database.Connection import Connection
from dataclasses import dataclass
from typing import TypeVar, Generic

T = TypeVar('T', bound=Connection)

@dataclass(frozen=True, slots=True)
class DataRepositoryMongoDB(DataRepository):
    connection: Generic[T]

    def add(self, data: DataOfEsp):
        # Converte a entidade DataOfEsp para um dicionário
        data_dict = {
            "humidity": data.humidity,
            "temperature": data.temperature,
            "conductivity": data.conductivity,
            "ph": data.ph,
            "nitrogen": data.nitrogen,
            "phosphorus": data.phosphorus,
            "potassium": data.potassium,
        }

        # Remove o campo _id se estiver presente para evitar duplicação
        if "_id" in data_dict:
            del data_dict["_id"]

        # Verifica se a conexão está ativa antes de adicionar os dados
        if self.connection.is_connected():
            self.connection.add(data=data_dict)
        else:
            raise ConnectionError("No active connection")

        return data_dict
