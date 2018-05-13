import requests
import threading
import time
from flask import Flask
app = Flask(__name__)

class Pinger (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            print("Performing request!")
            r = requests.get('http://springboot-sample:8085')
            # r = requests.get('http://localhost:8085')
            print(r.status_code)
            time.sleep(1)

@app.route('/')
def hello_world():
    return 'Flask Dockerized'

@app.route('/ping')
def ping():
    pinger = Pinger()
    pinger.start()
    return 'Pinger started!'

if __name__ == '__main__':
    app.run(debug=True, port=8086, host='0.0.0.0')
