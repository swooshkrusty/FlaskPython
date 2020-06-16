from flask import Flask


app = Flask (__name__)


@app.route('/')
def index():
    return "Hello application!!!"

@app.route('/david')
def devid():
    return "Hello, David!"


@app.route('/andrey')
def andrey():
    return "Hello, my dear Andrey! You are awesdwdwome!!!"


@app.route('/maria')
def maria():
    return "Hello, Maria!!! You are beauteful and amazing person!!!"
