from dataclasses import dataclass
from ...Application.usecases import GetDataOfEspByDate
from ..Repositories.DataOfEspRepository import DataRepositoryMongoDB
from ..Database.MongoConnection import MongoConnection

@dataclass(frozen=True, slots=True)
class GetByDateDataOfEspFactory():
    def create(self) -> GetDataOfEspByDate:
        mongo_connection = MongoConnection()
        mongo_connection.connect()
        
        return GetDataOfEspByDate(
            data_repository=DataRepositoryMongoDB(connection=mongo_connection)
        )