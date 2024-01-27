#!/usr/bin/python3
"""hello and nbnb
"""

from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello():
    """saying hello"""

    return ("Hello HBNB!")

@app.route("/hbnb", strict_slashes=False)
def disp():
    """saying hbnb"""

    return ("HBNB")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
