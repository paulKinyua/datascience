# from flask imp Flask
from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/hello")
def hello():
    return "Welcome my app."

app.run()