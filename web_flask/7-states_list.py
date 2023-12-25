#!/usr/bin/python3
''' This module runs a basic flask web application '''

from flask import Flask, render_template
from markupsafe import escape
from models import storage
from models.base_model import BaseModel
from models.state import State

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
    return 'C {}'.format(escape(text.replace('_', ' ')))


@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    ''' Variable text routing with default value '''
    return 'Python {}'.format(escape(text.replace('_', ' ')))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    ''' Returns a message if n is a number '''
    return '{} is a number'.format(escape(n))


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    ''' Returns an html page if n is an integer '''
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    ''' Returns an html page with odd or even depending on n '''
    return render_template('6-number_odd_or_even.html', n=n)


@app.route("/states_list", strict_slashes=False)
def list_states():
    ''' Displays an html page with a list of states '''
    return render_template('7-states_list.html', state_list=storage.all(State))


@app.teardown_appcontext
def tear_down(exc):
    ''' Takes care of tearing down the current session '''
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
