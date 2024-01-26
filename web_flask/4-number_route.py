#!/usr/bin/python3
"""hello and nbnb
"""

from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello():
    """saying hello
    """

    return ("Hello HBNB!")

@app.route("/hbnb", strict_slashes=False)
def disp():
    """saying hbnb
    """

    return ("HBNB")

@app.route("/c/<text>", strict_slashes=False)
def letter(text):
    """getting input
    """
    text = text.replace("_", " ")
    return ("C {}".format(text))

@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
def pytext(text="is cool"):
    """python writing
    """

    text = text.replace("_", " ")
    return ("Python {}".format(text))

@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """printing out a number
    """
    return ("{} is a number".format(n))


if __name__ == "__main__":
    app.run(host="0.0.0.0")
