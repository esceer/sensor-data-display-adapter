class WarehouseClient:
    from config.config import Config

    def __init__(self, connection_params: Config):
        import requests
        self._requests = requests
        self._connection_params = connection_params

    def get_sensor_state(self, name: str):
        fetch_response = self._requests.get(self._get_fetch_by_name_url(name))
        return ResponseParser.gather_sensor_value_from_response(fetch_response)

    def _get_fetch_all_url(self) -> str:
        return self._get_base_path() + '/'

    def _get_fetch_by_name_url(self, sensor_name: str) -> str:
        return self._get_base_path() + f'/name/{sensor_name}'

    def _get_base_path(self) -> str:
        return 'http://%s:%s/sensors' % (
            self._connection_params.get_warehouse_host(),
            self._connection_params.get_warehouse_port()
        )


class ResponseParser:
    from requests import Response

    @staticmethod
    def gather_sensor_value_from_response(response: Response) -> float:
        json = response.json()
        if 'state' in json:
            return float(json.get('state'))
        else:
            raise ValueError(f'Sensor state cannot be gathered from response: {json}')
