from dataclasses import dataclass
from ....__seedwork.Infrastructure.Database.Connection import Connection
from sqlalchemy import URL, create_engine
from sqlalchemy.orm import sessionmaker
from os import getenv

@dataclass(slots=True, frozen=True)
class MongoConnection(Connection):
    
    port: int = getenv("PORT_DB")
    username: str = getenv("USER_DB")
    password: str = getenv("PASSWD_DB")
    host: str = getenv("HOST_DB")
    database: str = getenv("DATABASE_DB")
    driver: str = getenv("DRIVER_DB")
    
    def __post_init__(self):
        # Inicializando a variável de engine e session para evitar o congelamento da classe
        object.__setattr__(self, 'engine', None)
        object.__setattr__(self, 'Session', None)

    def connect(self):
        """
        Conecta ao banco de dados PostgreSQL utilizando o SQLAlchemy e retorna a conexão.
        """
        url_obj = URL.create(
            drivername=self.driver,
            username=self.username,
            password=self.password,
            host=self.host,
            port=self.port,
            database=self.database
        )
        
        engine = create_engine(url_obj)
        session = sessionmaker(bind=engine)
        
        object.__setattr__(self, 'engine', engine.connect())
        object.__setattr__(self, 'Session', session)
        
        return self.engine
    
    def disconnect(self):
        """
        Desconecta a conexão atual se estiver conectada.
        """
        if not self.engine.closed:
            self.engine.close()
        else:
            return "Disconnected"
    
    def is_connected(self) -> bool:
        """
        Verifica se a conexão está ativa.
        """
        return not self.engine.closed if self.engine else False
    
    def query(self):
        """
        Retorna a sessão de consulta (query) do SQLAlchemy.
        """
        if self.is_connected():
            return self.Session()
        else:
            raise ConnectionError("No active connection")
    
    def rollback(self):
        """
        Realiza o rollback da transação atual.
        """
        if self.is_connected():
            session = self.query()
            session.rollback()
            session.close()
        else:
            raise ConnectionError("No active connection")
    
    def commit(self):
        """
        Realiza o commit da transação atual.
        """
        if self.is_connected():
            session = self.query()
            session.commit()
            session.close()
        else:
            raise ConnectionError("No active connection")
    
    def add(self, data_of_persistent):
        """
        Adiciona uma entidade ao banco de dados.
        """
        if self.is_connected():
            session = self.query()
            session.add(data_of_persistent)
            session.commit()
            session.refresh(data_of_persistent)
            session.close()
            return data_of_persistent
        else:
            raise ConnectionError("No active connection")
    
    def refresh(self, data_of_persistent):
        """
        Recarrega a entidade do banco de dados.
        """
        if self.is_connected():
            session = self.query()
            session.refresh(data_of_persistent)
            session.close()
        else:
            raise ConnectionError("No active connection")
