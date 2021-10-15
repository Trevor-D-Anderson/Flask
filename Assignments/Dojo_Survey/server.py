from logging import debug
from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'Survey'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=['POST'])
def form():
    print(request.form.getlist('check'))
    session['name'] = request.form.get('name')
    session['location'] = request.form.get('location')
    session['favLang'] = request.form.get('favLang')
    session['comments'] = request.form.get('comments')
    session['check'] = request.form.getlist('check')
    return redirect('/result')

@app.route('/result')
def results():
    checks = session['check']
    return render_template('results.html', checks=checks)

@app.route('/return', methods=['POST'])
def goHome():
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)