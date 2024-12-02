from ...__seedwork.Application.usecase import UseCase
from ...__seedwork.Domain.Exceptions.domain_exception import DomainException
from dataclasses import dataclass
from .Adapters.data_repository import DataRepository
from datetime import datetime
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
        
        
@dataclass(frozen=True, slots=True)
class GetDataOfEspByDate(UseCase):
    data_repository: DataRepository
    
    @dataclass(frozen=True, slots=True)
    class Input:
        initialDate: str
        finalDate: str
    
    @dataclass(frozen=True, slots=True)
    class Output:
        data: dict[DataOfEsp]
        success: bool
        message: str
        
    
    def execute(self, input:'Input') -> 'Output':
        try:
            initialDate = datetime.strptime(input.initialDate, "%Y-%m-%d")
            finalDate = datetime.strptime(input.finalDate, "%Y-%m-%d")
            data_of_esp = self.data_repository.get_by_date(initialDate,finalDate)
            return self.Output(message="Data retrieve successfuly", success=True, data=data_of_esp)
        except DomainException as e:
            return self.Output(message=e.message, success=False)    
        

@dataclass(frozen=True, slots=True)
class GetLastDataOfEsp(UseCase):
    data_repository: DataRepository
    
    @dataclass(frozen=True, slots=True)
    class Output:
        message: str
        data: DataOfEsp
        success: bool
        
    
    def execute(self) -> 'Output':
        try:
            data_of_esp = self.data_repository.get_last()
            print(data_of_esp)
            return self.Output(message="Data retrieve successfuly", success=True, data=data_of_esp)
        except DomainException as e:
            return self.Output(message=e.message, success=False)