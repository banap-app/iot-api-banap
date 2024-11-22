from ...__seedwork.Application.usecase import UseCase
from ...__seedwork.Domain.Exceptions.domain_exception import DomainException
from dataclasses import dataclass
from .Adapters.data_repository import DataRepository
from ..Domain.entities import DataOfEsp


@dataclass(frozen=True, slots=True)
class CreateNewDataOfEsp(UseCase):
    data_repository: DataRepository

    @dataclass(frozen=True, slots=True)
    class Input:
        humidity: float
        temperature: float
        conductivity: float
        ph: float
        nitrogen: float
        phosphorus: float
        potassium: float
        
    @dataclass(frozen=True, slots=True)
    class Output:
        message: str
        success: bool
    
    def execute(self, input: 'Input') -> 'Output':
        try:
            data_of_persistence = DataOfEsp(input.humidity, input.temperature, input.conductivity, input.ph, input.nitrogen, input.phosphorus, input.potassium)
            self.data_repository.add(data=data_of_persistence)
            return self.Output(message="Data saved successfully", success=True)
        except DomainException as e:
            return self.Output(message=e.message, success=False)    
        
        
