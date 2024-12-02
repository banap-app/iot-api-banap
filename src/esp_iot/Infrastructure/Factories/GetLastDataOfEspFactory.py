from dataclasses import dataclass
from ...Application.usecases import GetLastDataOfEsp
from ..Repositories.DataOfEspRepository import DataRepositoryMongoDB
from ..Database.MongoConnection import MongoConnection

@dataclass(frozen=True, slots=True)
class GetLastDataOfEspFactory():
    def create(self) -> GetLastDataOfEsp:
        mongo_connection = MongoConnection()
        mongo_connection.connect()
        
        return GetLastDataOfEsp(
            data_repository=DataRepositoryMongoDB(connection=mongo_connection)
        )