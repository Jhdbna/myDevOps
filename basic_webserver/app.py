# https://flask.palletsprojects.com/en/2.0.x/quickstart/

from flask import Flask
import os

from werkzeug.exceptions import abort

app = Flask(__name__)

counter = 0


@app.route("/")
def hello_world():
    return "<p>Hello, World! " + os.environ['HOSTNAME'] + "</p>"


@app.route("/healthz")
def hello():
    global counter

    if counter > 15:
        return abort(400, 'not ok')
    else:
        counter += 1
        return "ok"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
