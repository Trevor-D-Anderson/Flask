from logging import debug
from flask import Flask
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Hello World!"

@app.route("/Dojo")
def welcome():
    return "Dojo"
@app.route("/say/<name>")
def say(name):
    return f"Hi {name}"

if __name__ == "__main__":
    app.run(debug=True)
