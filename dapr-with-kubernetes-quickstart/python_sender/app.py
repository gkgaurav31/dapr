import time
import requests
import os
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')

n = 0

while True:
    n = (n + 1) % 1000000
    message = {"msg": "Hello, World! " + str(n)}

    logging.info(message)

    try:
        resp = requests.post(
            """http://localhost:3500/v1.0/invoke/nodereceiver/method/greeting""", json=message)
    except Exception as e:
        logging.error(e)
    time.sleep(5)
