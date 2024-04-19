#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask

app = Flask(__name__)

# define rout for url


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """display Hello HBNB!"""
    return "Hello HBNB!"


if __name__ == '__main__':
    # listening on all available nertwork interfaces (0.0.0.0) on port 5000
    app.run(host='0.0.0.0', port='5000')
