from flask import Flask, render_template


app = Flask (__name__)


@app.route('/')
def index ():
    names = ["Alice", "Bob", "Charlie", "Andrey", "Maria"]
    return render_template('index7.html', names=names)
