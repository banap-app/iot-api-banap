from dataclasses import dataclass
from ...Application.usecases import CreateNewDataOfEsp
from ..Repositories.DataOfEspRepository import DataRepositoryMongoDB
from ..Database.MongoConnection import MongoConnection

@dataclass(frozen=True, slots=True)
class CreateNewDataOfEspFactory():
    def create(self) -> CreateNewDataOfEsp:
        
        return CreateNewDataOfEsp(
            data_repository=DataRepositoryMongoDB(connection=MongoConnection)
        )