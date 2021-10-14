from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)  
app.secret_key = 'Great Numbers!'

@app.route('/')
def index():
    if 'guess' and 'guesses' in session:
        print('key exists!')
    else:
        session['guess'] = random.randrange(1,100)
        session['guesses'] = []
        print("key 'guess' was just made")
    return render_template("index.html")

@app.route('/Reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

@app.route('/check', methods=['POST'])
def check():
    if int(request.form['check']) == session['guess']:
        print("You Win!")
        session['value'] = "Win"
        return redirect('/leaderboard')
    if len(session['guesses']) >= 4:
        session['value'] == 'Lose'
        return redirect('https://www.youtube.com/watch?v=QUzvs6gdrbo&ab_channel=Vidmanheart')
    elif int(request.form['check']) > session['guess']:
        print('nope too high')
        session['value'] = "High"
        session['guesses'].append(int(request.form['check']))
        return redirect('/')
    elif int(request.form['check']) < session['guess']:
        print('nope too low')
        session['value'] = "Low"
        session['guesses'].append(int(request.form['check']))
        return redirect('/')

@app.route('/leaderboard')
def leaderboard():
    return render_template("leaderboard.html")

@app.route('/leadername')
def leaderName():
    


if __name__=="__main__":   
    app.run(debug=True)  