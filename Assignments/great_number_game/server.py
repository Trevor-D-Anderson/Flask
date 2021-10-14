from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = 'my keys!'

@app.route('/')         
def index():
    if 'key_name' and 'total' in session:
        session['key_name']+=1
        print('key exists!')
    else:
        session['key_name'] = 1
        session['total'] = 0
        print("key 'key_name' does NOT exist")
    totalCom = int(session['key_name']) + int(session['total'])
    return render_template("index.html", totalCom=totalCom)

@app.route('/addTwo', methods=['POST'])
def addTwo():
    session['total']+=2
    print('total works')

    return redirect('/')

@app.route('/Reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

@app.route('/add', methods=['POST'])
def add():
    session['total'] += int(request.form['value'])
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True)  