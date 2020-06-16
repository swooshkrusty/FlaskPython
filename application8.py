from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route('/')
def index8():
    return render_template('index8.html')

@app.route('/more8')
def more8():
    return render_template('more8.html')
