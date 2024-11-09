import sys
import os
from bootstrap import create_app
from src.esp_iot.Infrastructure.Database.MongoConnection import MongoConnection
current_script_path = os.path.realpath(__file__)
current_directory = os.path.dirname(current_script_path)
sys.path.append(current_directory)

connection = MongoConnection()
connection.connect()
connection.add(data={})

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)