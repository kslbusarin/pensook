
from flask import Flask, request,url_for, redirect, render_template ,session
import os

app = Flask(__name__)
@app.route('/')
def login():
        return render_template('login.html')
@app.route('/loginc',methods=['POST'])
def loginc():
    if request.method=="POST":
        username=request.form['usernametxt']
        password=request.form['passwordtxt']
        usertxt= 'root'
        passtxt= '1234'
        if usertxt==username and passtxt==password:
              session['user'] = username
              user=session.get('user')
              return render_template('lobby.html',user=user)
        else:
             return render_template('login.html')
        
@app.route('/logout')
def logout():
    session.pop("user",None)
    return redirect(url_for("login"))   

@app.route('/save', methods=['POST'])
def save(): 
    x = dict(request.form.items())
    water = 10 - int(x['water'])
    rice = 6 - int(x['rice'])
    banana = 12 - int(x['banana'])
    bread = 5 - int(x['bread'])
    milk = 3 - int(x['milk'])
    return render_template('stock.html',water=water,rice=rice,banana=banana,bread=bread,milk=milk)


    

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True)