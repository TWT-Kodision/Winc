__winc_id__ = "cc1b724762854e85a8defa04287f708b"
__human_name__ = "requests"
from flask import Flask

app = Flask(__name__)

@app.route("/")
def Home():
    return "<p>Home, sweet home.</p>"

@app.route("/greet")
def Greet():
    return "<h1>Hello, world!</h1>"

@app.route("/greet/name")
def GreetName():
    return "<h1>hello you!</h1>"