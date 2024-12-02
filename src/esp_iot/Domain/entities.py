from dataclasses import dataclass, field, fields
from typing import Optional
from datetime import datetime, timedelta
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
    created_at: Optional[datetime] = field(default=None)
    updated_at: Optional[datetime] = field(default=None)

    def __post_init__(self):
        # Calcula o horário do Brasil (UTC-3)
        now = datetime.utcnow() - timedelta(hours=3)
        
        # Atribui os valores de created_at e updated_at
        object.__setattr__(self, "created_at", now)
        object.__setattr__(self, "updated_at", now)

        # Valida os campos
        errors = self.validate()
        if errors:
            raise DomainException(f"Validation: {errors}")

    def validate(self):
        errors = []
        for field_ in fields(self):
            value = getattr(self, field_.name)
            if isinstance(value, float) and value < 0.0:
                errors.append(f"{field_.name} cannot be negative.")
        return errors
