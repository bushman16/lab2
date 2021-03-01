import requests
import json
import time
d = {}
def zapros():
    b = requests.get('https://blockchain.info/ru/ticker').text
    d = json.loads(b)
    while True:
        f = input()
        for key in d:
            if key == f:
                print(key, d[key])
        time.sleep(5)
zapros()
