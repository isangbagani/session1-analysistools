import os
import hashlib
from flask import Flask, request, render_template, redirect, session, url_for

app = Flask(__name__)
app.secret_key = 'ING Forever'

@app.route('/')
def index():
    session['loggedin'] = False
    session['username'] = ''
    return render_template('login.html',header='Session 1')

@app.route('/login', methods=['GET','POST'])
def login(): 
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        if 'username' in request.form and 'password' in request.form:
            username = request.form['username']
            password = request.form['password']
            hashedpass= hashlib.md5(password.encode())
            print(hashedpass.hexdigest())

        if username == 'admin' and hashedpass.hexdigest() == 'd9b23ebbf9b431d009a20df52e515db5':
            session['loggedin'] = True
            session['username'] = username
            return redirect(url_for('main'))
           
        return render_template('login.html', msg='Invalid credentials')


@app.route('/main')
def main():
    if session['loggedin'] == True:
        return render_template('main.html')
    return render_template('login.html', msg='Please login')

@app.route('/members')
def members():
    if session['loggedin'] == True:
        return render_template('members.html',username='admin')
    return render_template('login.html', msg='Please login')

@app.route('/arzon')
def arzon():
    if session['loggedin'] == True:
        return render_template('arzon.html',username='admin')
    return render_template('login.html', msg='Please login')

@app.route('/darkstorm')
def darkstorm():
    if session['loggedin'] == True:
        return render_template('darkstorm.html',username='admin')
    return render_template('login.html', msg='Please login')

@app.route('/leoric')
def leoric():
    if session['loggedin'] == True:
        return render_template('leoric-rot13.html')
    return render_template('login.html', msg='Please login')

@app.route('/logout')
def logout():
    session.pop('loggedin', False)
    session.pop('username', '')
    #conn.close()
    return redirect(url_for('index'))

if __name__ == "__main__":
    #website_url = 'session1.demo:8000'
    #app.config['SERVER_NAME'] = website_url
    app.run(host='0.0.0.0',port='8000',debug=False)
    