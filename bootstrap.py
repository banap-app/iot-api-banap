from flask import Flask
from src.esp_iot.Infrastructure.Factories.CreateNewDataOfEspFactory import CreateNewDataOfEspFactory
from src.esp_iot.Infrastructure.Factories.GetByDateDataOfEspFactory import GetByDateDataOfEspFactory
from src.esp_iot.Infrastructure.Http.router import FlaskRouter
from src.esp_iot.Infrastructure.Adapters.request_adapter import SimpleRequest
from src.esp_iot.Infrastructure.Adapters.response_adapter import SimpleResponse
from src.esp_iot.Infrastructure.Http.Api.CreateNewDataOfEspController import CreateNewDataOfEspController
from src.esp_iot.Infrastructure.Http.Api.GetByDateDataOfEspController import GetByDateDataOfEspController

def create_app():
    app = Flask(__name__)

    create_data_of_esp_factory = CreateNewDataOfEspFactory()
    get_by_date_data_of_esp_factory = GetByDateDataOfEspFactory()

    router = FlaskRouter(app)

    def create_data_of_esp_controller_method(request: SimpleRequest) -> SimpleResponse:
        controller = CreateNewDataOfEspController(create_data_use_case=create_data_of_esp_factory.create())
        return controller.handle(request)

    def get_by_date_data_of_esp_controller_method(request: SimpleRequest) -> SimpleResponse:
        controller = GetByDateDataOfEspController(get_data_use_case=get_by_date_data_of_esp_factory.create())
        return controller.handle(request)

    # Adiciona as rotas
    router.add_route('/data_of_esp', create_data_of_esp_controller_method, methods=['POST'])
    router.add_route('/get_by_date_data_of_esp', get_by_date_data_of_esp_controller_method, methods=['GET'])

    return app
