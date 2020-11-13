import json

from bottle import response, Bottle

from utils.actuator import Actuator


def make_wsgi_app(actuator: Actuator):
    app = Bottle()

    @app.get('/sensors')
    @app.get('/sensors/<name>')
    def list_sensors_handler(name: str = None):
        '''Handles sensor listing'''
        response.headers['Content-Type'] = 'application/json'
        response.headers['Cache-Control'] = 'no-cache'
        sensor_state = actuator.is_above_threshold(name)
        return json.dumps({'state': list(_names)})

    return app
