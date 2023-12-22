#!/usr/bin/python3
''' This module runs a basic flask web application '''

from flask import Flask, escape
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    ''' Returns a simple hello text '''
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    ''' Returns a simple text '''
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    ''' Variable text routing '''
    return 'C {}'.format(escape(text))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
