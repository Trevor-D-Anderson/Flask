from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.survey import Survey

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=['POST'])
def form():

    if not Survey.validate_survey(request.form):
        return redirect('/')
    
    data = {
    "name": request.form['name'],
    "location": request.form['location'],
    "language": request.form['language'],
    "comment": request.form['comment']
    }
    Survey.new_survey(data)
    return redirect('/result')

@app.route('/result')
def results():
    return render_template('results.html', survey=Survey.get_survey())

@app.route('/return', methods=['POST'])
def goHome():
    return redirect('/')