from flask import Flask


app = Flask(__name__)


@app.route('/')
def index ():
    return "Hello, world and application number 3!!!"


@app.route('/<string:name>')
def hello(name):
    return f"Hello, my dear {name}!!!"
