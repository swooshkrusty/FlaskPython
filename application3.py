from flask import Flask


app = Flask(__name__)


@app.route('/')
def index ():
    return "Hello, world and application number 3!!!"


@app.route('/<string:name>')
def hello(name):
    name = name.capitalize()
    return f"<h1>Hello, my dear {name}!!!</h1><br>hey!!!"
