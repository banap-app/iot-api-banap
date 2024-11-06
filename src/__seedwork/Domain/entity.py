from abc import ABC
from dataclasses import asdict, dataclass

@dataclass(frozen=True, slots=True)
class Entity(ABC):
    
    def to_dict(self):
        return asdict(self)
    
    def get(self, prop_name: str):
        try:
            return getattr(self, prop_name)
        except AttributeError:
            raise ValueError(f"Property '{prop_name}' does not exist in {self.__class__.__name__}")
        
    def set(self, prop_name: str, value):
        if not hasattr(self, prop_name):
            raise ValueError(f"Property '{prop_name}' does not exist in {self.__class__.__name__}")
        object.__setattr__(self, prop_name, value)