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
        print(methods)
        view_func = self.handle_request(controller_method, path, methods)
        return self.app.add_url_rule(path, view_func=view_func, methods=methods)

    def handle_request(self, controller_method: Callable, path: str, methods):
        def wrapper():
            try:
                # Se for uma requisição POST, obter o corpo JSON
                if 'POST' in methods:
                    request_data = request.json
                # Se for uma requisição GET, obter parâmetros da query string
                elif 'GET' in methods:
                    request_data = request.args.to_dict()  # Obtém parâmetros da URL (query string)
                else:
                    raise ValueError("Unsupported HTTP method")

                # Cria um SimpleRequest com os dados obtidos
                simple_request = SimpleRequest(data=request_data)
                response: SimpleResponse = controller_method(simple_request)

                # Verifica se a resposta foi bem-sucedida
                if response.is_success():
                    return jsonify(response.get_data()), 200
                else:
                    return jsonify(response.get_data()), 400

            except KeyError as e:
                # Tratando erros de chaves faltando no request
                error_response = SimpleResponse()
                error_response.set_data({
                    "message": f"Missing field {str(e)}",
                    "success": False
                })
                return jsonify(error_response.get_data()), 400

            except Exception as e:
                # Tratando outros erros
                error_response = SimpleResponse()
                error_response.set_data({
                    "message": f"An error occurred: {str(e)}",
                    "success": False
                })
                return jsonify(error_response.get_data()), 500

        # Atribui um nome único à função
        wrapper.__name__ = f"view_func_{path.strip('/').replace('/', '_')}"
        return wrapper
