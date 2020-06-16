from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index10():
    return render_template("index10.html")

@app.route("/hello10", methods=["GET","POST"])
def hello10():
    if request.method == "GET":
        return "Please submit the form instead"
    else:
        name = request.form.get("name")
        return render_template("hello10.html", name=name)
