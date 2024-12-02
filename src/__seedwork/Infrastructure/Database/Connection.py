from abc import ABC, abstractmethod


class Connection(ABC):
    @abstractmethod
    def connect(self):
        raise NotImplementedError("connect should not be implemented")
    
    def disconnect(self):
        raise NotImplementedError("disconnect should not be implemented")
    
    def is_connected(self):
        raise NotImplementedError("is_connected should not be implemented")
    
    def add(self):
        raise NotImplementedError("add should not be implemented")
    
    def commit(self):
        raise NotImplementedError("commit should not be implemented")
    
    def rollback(self):
        raise NotImplementedError("rollback should not be implemented")
    
    def refresh(self):
        raise NotImplementedError("refresh should not be implemented")
    
    def query(self):
        raise NotImplementedError("query should not be implemented")