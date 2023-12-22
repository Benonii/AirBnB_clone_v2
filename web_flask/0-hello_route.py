#!/usr/bin/python3
''' This module runs a basic flask web application '''

from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello_hbnb():
    ''' Returns a simple html text '''
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
