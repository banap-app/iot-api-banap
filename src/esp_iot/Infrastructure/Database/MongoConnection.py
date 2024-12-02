from dataclasses import dataclass
from pymongo import MongoClient, errors
from os import getenv
from dotenv import load_dotenv
from datetime import datetime

@dataclass
class MongoConnection:
    load_dotenv()
    port: int = int(getenv("PORT_DB"))
    driver: str = getenv("DRIVER_DB")
    username: str = getenv("USER_DB")
    password: str = getenv("PASSWD_DB")
    host: str = getenv("HOST_DB")
    database: str = getenv("DATABASE_DB")
    collection_name: str = getenv("COLLECTION_DB")

    def __post_init__(self):
        self.client = None
        self.db = None
        self.collection = None

    def connect(self):
        """
        Conecta ao banco de dados MongoDB utilizando o pymongo e retorna a conexão.
        Se não conectar dentro de 10 segundos, lança uma exceção.
        """
        # URI utilizando o DRIVER_DB configurado no .env
        uri = f"{self.driver}{self.username}:{self.password}@{self.host}/{self.database}?retryWrites=true&w=majority&appName=Cluster0"
    
        try:
            print(f"Tentando conectar com a URI: {uri}")  # Para debugging
            self.client = MongoClient(uri, serverSelectionTimeoutMS=10000)
            # Testando a conexão
            self.client.admin.command('ping')
            self.db = self.client[self.database]
            self.collection = self.db[self.collection_name]
            print("Conexão com o MongoDB estabelecida com sucesso.")
            return self.db
        except errors.ServerSelectionTimeoutError as e:
            raise ConnectionError(f"Erro de timeout ao conectar ao MongoDB: {e}")
        except errors.InvalidURI as e:
            raise ConnectionError(f"Erro na URI de conexão: {e}")
    
    def disconnect(self):
        """
        Desconecta a conexão atual se estiver conectada.
        """
        if self.client:
            self.client.close()
            self.client = None
        else:
            return "Disconnected"
    
    def is_connected(self) -> bool:
        """
        Verifica se a conexão está ativa.
        """
        return self.client is not None and self.client.admin.command('ping')['ok'] == 1
    
    def query(self, filter: dict = None, sort: list = None, limit: int = None):
        """
        Retorna a coleção com base no filtro para realizar consultas.
        O filtro pode incluir qualquer campo e suas operações.
        """
        if not self.is_connected():
            raise ConnectionError("No active connection")
        
        if filter is None:
            filter = {}

        # Realiza a consulta com o filtro passado
        cursor = self.collection.find(filter)
        
        # Se houver um critério de ordenação
        if sort:
            cursor = cursor.sort(sort)
        
        # Limita o número de resultados, se necessário
        if limit:
            cursor = cursor.limit(limit)

        return cursor
    
    def add(self, data):
        """
        Adiciona uma entidade ao banco de dados.
        """
        if self.is_connected():
            result = self.collection.insert_one(data)
            return result.inserted_id
        else:
            raise ConnectionError("No active connection")
    
    def refresh(self, query):
        """
        Recarrega a entidade do banco de dados.
        """
        if self.is_connected():
            return self.collection.find_one(query)
        else:
            raise ConnectionError("No active connection")
    
    def rollback(self):
        """
        Realiza o rollback da transação atual.
        """
        raise NotImplementedError("MongoDB não suporta transações da mesma forma que bancos de dados relacionais.")
    
    def commit(self):
        """
        Realiza o commit da transação atual.
        """
        raise NotImplementedError("MongoDB não suporta transações da mesma forma que bancos de dados relacionais.")
    
