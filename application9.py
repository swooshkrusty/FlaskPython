from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index9():
    return render_template("index9.html")


@app.route('/more9')
def more9():
    return render_template("more9.html")
