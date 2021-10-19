from flask import Flask
from flask_cors import CORS,cross_origin
import datetime
import math
import json

app = Flask(__name__)

CYCLES_PER_MINUTE = 1

@app.route("/")
@cross_origin(origin='*', headers=[])
def main():
    epoch = datetime.datetime.now().timestamp()
    response_dict = {
        "co2_ppm": 800 + 300 * math.sin( CYCLES_PER_MINUTE * math.pi * epoch / 30 ),
        "temperature_c": 20 - 5 * math.sin( CYCLES_PER_MINUTE * math.pi * epoch / 30 ),
        "pressure_mbar": 0
    }
    return json.dumps(response_dict)

