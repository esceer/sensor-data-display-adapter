from clients.warehouse_client import WarehouseClient
from config.config import Config


class Actuator:

    def __init__(self, sensor_threshold_registry: Config, warehouse_client: WarehouseClient):
        self._sensor_threshold_registry = sensor_threshold_registry
        self._warehouse_client = warehouse_client

    def is_above_threshold(self, sensor_name: str):
        sensor_state = self._warehouse_client.get_sensor_state(sensor_name)
        threshold = self._sensor_threshold_registry.get_threshold_for(sensor_name)
        return sensor_state > threshold
