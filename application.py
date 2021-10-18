from flask import Flask
import datetime
import math
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    second = datetime.datetime.now().second
    response_dict = {
        "co2_ppm": 800 + 300 * math.sin( math.pi * second / 30 ),
        "temperature_c": 0,
        "pressure_mbar": 0
    }
    return json.dumps(response_dict)

