import configparser


class Config:
    def __init__(self):
        self._config_file_path = '../resources/sdda.ini'
        self._config = self._parse_config_file()

    def get_server_port(self) -> str:
        return self._config['Server']['port']

    def get_warehouse_host(self) -> str:
        return self._config['Warehouse']['host']

    def get_warehouse_port(self) -> str:
        return self._config['Warehouse']['port']

    def get_threshold_for(self, sensor_name) -> float:
        return float(self._config['Thresholds'][sensor_name])

    def _parse_config_file(self) -> configparser.ConfigParser:
        config = configparser.ConfigParser()
        config.read(self._config_file_path)
        return config
