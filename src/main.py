import bottle

from api import api
from clients.warehouse_client import WarehouseClient
from config.config import Config
from utils.actuator import Actuator

app = application = bottle.default_app()

if __name__ == '__main__':
    config = Config()
    warehouse_client = WarehouseClient(config)
    actuator = Actuator(config, warehouse_client)
    bottle.run(api.make_wsgi_app(actuator), host='127.0.0.1', port=8050)
