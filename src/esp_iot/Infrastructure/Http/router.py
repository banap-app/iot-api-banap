from ....__seedwork.Infrastructure.Http.router import IRouter
from dataclasses import dataclass
from flask import Flask, request, jsonify
from typing import Callable
from ..Adapters.request_adapter import SimpleRequest
from ..Adapters.response_adapter import SimpleResponse


@dataclass(frozen=True, slots=True)
class FlaskRouter(IRouter):
    app: Flask

    def add_route(self, path: str, controller_method: Callable, methods=['POST']):
        return self.app.add_url_rule(path, view_func=controller_method, methods=methods)

    def handle_request(self, controller_method: Callable):
        def wrapper():
            try:
                request_data = request.json

                simple_request = SimpleRequest(data=request_data)
                response: SimpleResponse = controller_method(simple_request)

                # Verifica se a resposta foi bem sucedida com base no método is_success
                if response.is_success():
                    # Retorna os dados da resposta
                    return jsonify(response.get_data()), 200
                else:
                    # Se a resposta indicou falha, retorna 400 ou o código apropriado
                    return jsonify(response.get_data()), 400


            except KeyError as e:
                error_response = SimpleResponse()
                error_response.set_data({
                    "message": f"Missing field {str(e)}",
                    "success": False
                })
                return jsonify(error_response.get_data()), 400

            except Exception as e:
                error_response = SimpleResponse()
                error_response.set_data({
                    "message": f"An error occurred: {str(e)}",
                    "success": False
                })
                return jsonify(error_response.get_data()), 500

        return wrapper
