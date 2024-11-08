from flask import Flask
from src.esp_iot.Infrastructure.Factories.CreateNewDataOfEspFactory import CreateNewDataOfEspFactory
from src.esp_iot.Infrastructure.Http.router import FlaskRouter
from src.esp_iot.Infrastructure.Adapters.request_adapter import SimpleRequest
from src.esp_iot.Infrastructure.Adapters.response_adapter import SimpleResponse
from src.esp_iot.Infrastructure.Http.Api.CreateNewDataOfEspController import CreateNewDataOfEspController

def create_app():
    app = Flask(__name__)
    
    
    create_data_of_esp_factory = CreateNewDataOfEspFactory()
    
    router = FlaskRouter(app)
    
    def create_data_of_esp_controller_method(request: SimpleRequest)-> SimpleResponse:

        controller = CreateNewDataOfEspController(create_data_use_case=create_data_of_esp_factory.create())
    
        return controller.handle(request)
    
    router.add_route('/data_of_esp', router.handle_request(create_data_of_esp_controller_method), methods=['POST'])
    
    return app