from flask import Flask, render_template, request, redirect, url_for
# import inline

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/user")
def user():
    return render_template("user.html")
