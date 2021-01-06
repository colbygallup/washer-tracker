from flask.json import jsonify
from sensors.vibration_sensor import VibrationSensor
from sensor import Sensor

from flask import Flask


app: Flask = Flask(__name__)

sensor: Sensor = VibrationSensor()
sensor.register(app)


@app.route('/', methods=['GET'])
def index() -> str:
    return 'test'


@app.route('/washers', methods=['GET'])
def washers() -> str:
    return jsonify({i: sensor.get_washer(i).name for i in range(10)})
