from collections import defaultdict
from typing import Dict
import time

from flask import Flask, request


app: Flask = Flask(__name__)
washers: Dict[int, int] = defaultdict(lambda: False)


@app.route('/update', methods=['POST'])
def update() -> str:
    data: Dict = request.get_json()
    try:
        washers[int(data['washer_id'])] = time.time()  # seconds since epoch
        return 'success'
    except ValueError:
        return 'fail'


@app.route('/', methods=['GET'])
def index() -> str:
    out: str = "<ul>"
    for key, value in washers.items():
        out += "<li>{}: {}</li>".format(key, time.time() - value <= 30)
    out += "</ul>"
    return out
