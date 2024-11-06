from dataclasses import dataclass, fields
from typing import Optional
from ...__seedwork.Domain.entity import Entity
from ...__seedwork.Domain.Exceptions.domain_exception import DomainException


@dataclass(frozen=True, slots=True)
class DataOfEsp(Entity):
    humidity: Optional[float] = 0.0
    temperature: Optional[float] = 0.0
    conductivity: Optional[float] = 0.0
    ph: Optional[float] = 0.0
    nitrogen: Optional[float] = 0.0
    phosphorus: Optional[float] = 0.0
    potassium: Optional[float] = 0.0
    
    def __post_init__(self):
        errors = self.validate()
        if errors:
            raise DomainException(f"Validation: {errors}")

    def validate(self):
        errors = []
        for field in fields(self):
            value = getattr(self, field.name)
            if value < 0.0:
                errors.append(f"{field.name} cannot be negative.")
        return errors
