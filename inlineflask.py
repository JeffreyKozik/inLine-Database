from flask import Flask
from markupsafe import escape
from flask import render_template

app = Flask(__name__)

@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name=name)
