from dataclasses import dataclass
from ....Application.usecases import GetLastDataOfEsp
from ....Infrastructure.Adapters.request_adapter import IRequest
from ....Infrastructure.Adapters.response_adapter import IResponse
from ...Adapters.response_adapter import SimpleResponse
from ...Adapters.request_adapter import SimpleRequest

@dataclass(frozen=True, slots=True)
class GetLastDataOfEspController:
    get_last_data_use_case:GetLastDataOfEsp

    def handle(self, request: IRequest) -> IResponse:


        try:
        
            output = self.get_last_data_use_case.execute()
            
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
