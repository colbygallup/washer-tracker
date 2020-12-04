from typing import NoReturn
import time

import RPi.GPIO as GPIO
import requests


def on_vibrate(channel) -> NoReturn:
    requests.post('http://10.1.5.118/update', json={'washer_id': 0})
    time.sleep(5)


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect()
