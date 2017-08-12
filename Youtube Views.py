from flask import Flask
from datetime import datetime



api_key = "AIzaSyDraPMr8KRfkux5u9DgCjfWh1SA_xJmIl8"
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/top10views', methods=["GET"])
def top10views():
    pass

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
