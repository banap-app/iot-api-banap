import sys
import os
import awsgi
from bootstrap import create_app
from src.esp_iot.Domain.entities import DataOfEsp
from src.esp_iot.Infrastructure.Database.MongoConnection import MongoConnection

current_script_path = os.path.realpath(__file__)
current_directory = os.path.dirname(current_script_path)
sys.path.append(current_directory)

app = create_app()

def lambda_handler(event, context):
    return awsgi.response(app, event, context)

# Execução local (para desenvolvimento/testes)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


