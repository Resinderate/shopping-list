#!/usr/bin/env python
from flask import Flask


app = Flask(__name__)

@app.route("/grocery/")
def hello_world():
    return "Shopping list v2!"
