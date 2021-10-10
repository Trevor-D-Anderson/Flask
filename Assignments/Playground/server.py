from logging import debug
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/play")
def playBox():
    # boxes = 3
    return render_template("index.html", boxes=3)

@app.route("/play/<int:boxes>")
def playBoxes(boxes):
    return render_template("index.html", boxes=boxes)

@app.route("/play/<int:boxes>/<color>")
def playBoxesColor(boxes, color):
    return render_template("index.html", boxes=boxes, color=color)

if __name__=="__main__":
    app.run(debug=True)