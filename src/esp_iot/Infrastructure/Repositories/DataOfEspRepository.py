from ...Domain.entities import DataOfEsp
from ...Application.Adapters.data_repository import DataRepository
from ....__seedwork.Infrastructure.Database.Connection import Connection
from dataclasses import dataclass
from datetime import datetime
from typing import TypeVar, Generic, List

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
            "created_at": data.created_at,
            "updated_at": data.updated_at,
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

    def get_by_date(self, initialDate: datetime, finalDate: datetime) -> List[DataOfEsp]:
        """
        Retorna os dados de DataOfEsp entre as datas fornecidas.
        """
        # Certifica que as datas estão no formato adequado
        start_of_day = datetime(
            initialDate.year, initialDate.month, initialDate.day)
        end_of_day = datetime(finalDate.year, finalDate.month,
                              finalDate.day, 23, 59, 59, 999999)

        # Cria o filtro para consulta entre as duas datas
        query = {
            "created_at": {
                "$gte": start_of_day,  # Maior ou igual a initialDate
                "$lte": end_of_day     # Menor ou igual a finalDate
            }
        }

        # Verifica se a conexão está ativa antes de consultar os dados
        if self.connection.is_connected():
            results = self.connection.query(query)
            results = list(results)

            for result in results:
                if '_id' in result:
                    result['_id'] = str(result['_id'])

        else:
            raise ConnectionError("No active connection")

        # Retorna os resultados obtidos da consulta
        return results

    def get_all(self) -> List[DataOfEsp]:
        return super().get_all()

    def get_last(self) -> DataOfEsp:
        """
        Retorna o último registro de DataOfEsp com base no campo created_at.
        """
        # Define a consulta para ordenar por 'created_at' em ordem decrescente
        query = {}
        sort_order = [("created_at", -1)]  # -1 para ordem decrescente

        # Verifica se a conexão está ativa antes de consultar os dados
        if self.connection.is_connected():
            result = self.connection.query(query, sort=sort_order, limit=1)

            # Converte o resultado em um objeto DataOfEsp, se existir
            if result:
                data = result[0]  # Pega o único item retornado
                return DataOfEsp(
                    humidity=data["humidity"],
                    temperature=data["temperature"],
                    conductivity=data["conductivity"],
                    ph=data["ph"],
                    nitrogen=data["nitrogen"],
                    phosphorus=data["phosphorus"],
                    potassium=data["potassium"],
                    created_at=data["created_at"],
                    updated_at=data["updated_at"]
                )
            else:
                raise ValueError("No data found")
        else:
            raise ConnectionError("No active connection")
