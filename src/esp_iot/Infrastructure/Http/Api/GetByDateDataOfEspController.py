from dataclasses import dataclass
from ....Application.usecases import GetDataOfEspByDate
from ....Infrastructure.Adapters.request_adapter import IRequest
from ....Infrastructure.Adapters.response_adapter import IResponse
from ...Adapters.response_adapter import SimpleResponse
from ...Adapters.request_adapter import SimpleRequest

@dataclass(frozen=True, slots=True)
class GetByDateDataOfEspController:
    get_data_use_case:GetDataOfEspByDate

    def handle(self, request: IRequest) -> IResponse:
        
        data = request.get_data()
        print(data)

        try:
            # Criando o input para o use case
            input_data = self.get_data_use_case.Input(
                initialDate=data['initialDate'],
                finalDate=data['finalDate']
            )
            
            
            # Executando o use case
            output = self.get_data_use_case.execute(input_data)
            
            # Criando a resposta
            response = SimpleResponse()
            response.set_data({
                "message": output.message,
                "success": output.success,
                "data": output.data
            })
            
            
            return response
        
        except KeyError as e:
            # Tratando erros de chaves faltando no request
            response = SimpleResponse()
            response.set_data({
                "message": f"Missing field: {str(e)}",
                "success": False
            })
            return response
        
        except Exception as e:
            # Tratando outros erros
            response = SimpleResponse()
            response.set_data({
                "message": f"An error occurred: {str(e)}",
                "success": False
            })
            return response
