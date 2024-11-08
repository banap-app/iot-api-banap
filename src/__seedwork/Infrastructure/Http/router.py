from abc import ABC, abstractmethod

class IRouter(ABC):
    
    @abstractmethod
    def add_route(self, path: str, controller_method):
        pass

    @abstractmethod
    def handle_request(self, request):
        pass    