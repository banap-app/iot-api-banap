from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class CreateNewDataOfEspController:
    create_data_use_case:CreateNewDataOfEsp
    def __init__(self, create_data_use_case:CreateNewDataOfEsp):
        self.create_data_use_case = create_data_use_case

    def handle(self, request: IRequest) -> IResponse:
        data = request.get_data()

        try:
            # Criando o input para o use case
            input_data = self.use_case.Input(
                humidity=data["humidity"],
                temperature=data["temperature"],
                conductivity=data["conductivity"],
                ph=data["ph"],
                nitrogen=data["nitrogen"],
                phosphorus=data["phosphorus"],
                potassium=data["potassium"]
            )
            
            # Executando o use case
            output = self.use_case.execute(input_data)
            
            # Criando a resposta
            response = SimpleResponse()
            response.set_data({
                "message": output.message,
                "success": output.success
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
