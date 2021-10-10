from logging import debug
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<int:x>")
def indexRows(x):
    return render_template("checkerboard.html",x = x)

@app.route("/<int:x>/<int:y>")
def indexColumns(x,y):
    return render_template("checker.html",x = x, y=y)

@app.route("/<int:x>/<int:y>/<color1>/<color2>")
def indexColor(x,y,color1,color2):
    return render_template("checkercolor.html",x = x, y=y, color1=color1, color2=color2)

if __name__=="__main__":
    app.run(debug=True)