from ...Domain.entities import DataOfEsp
from ...Application.Adapters.data_repository import DataRepository
from ..Models.DataOfEspModelAlchemy import DataOfEspModel
from ....__seedwork.Infrastructure.Database.Connection import Connection
from dataclasses import dataclass
from typing import TypeVar, Generic

T = TypeVar('T', bound=Connection)


@dataclass(frozen=True, slots=True)
class DataRepositoryMongoDB(DataRepository):
    connection: Generic[T]

    def add(self, data_of_persistent: DataOfEsp):
        data = DataOfEspModel(
            humidity=data_of_persistent.get('humidity'),
            temperature=data_of_persistent.get('temperature'),
            conductivity=data_of_persistent.get('conductivity'),
            ph=data_of_persistent.get('ph'),
            nitrogen=data_of_persistent.get('nitrogen'),
            phosphorus=data_of_persistent.get('phosphorus'),
            potassium=data_of_persistent.get('potassium'),
        )

        self.connection.add(data)
        self.connection.commit()
        self.connection.refresh()
        return data
