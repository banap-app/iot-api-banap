from dataclasses import dataclass
from pymongo import MongoClient
from os import getenv
from dotenv import load_dotenv

@dataclass
class MongoConnection:
    load_dotenv()
    port: int = int(getenv("PORT_DB"))
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
        """
        uri = f"mongodb://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"
        self.client = MongoClient(uri)
        self.db = self.client[self.database]
        self.collection = self.db[self.collection_name]
        
        return self.db
    
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
    
    def query(self):
        """
        Retorna a coleção para realizar consultas.
        """
        if self.is_connected():
            return self.collection
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
