#!/usr/bin/python3
''' This module runs a basic flask web application '''

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    ''' Returns a simple hello text '''
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    ''' Returns a simple text '''
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
