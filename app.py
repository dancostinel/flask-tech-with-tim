import os
from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

@app.route('/')
def homepage():
    return render_template('index.html', name=__name__)

@app.route('/login', methods=('POST', 'GET'))
def login():
    if 'POST' == request.method:
        user_name: str = request.form['name']
        session['user_name'] = user_name
        return redirect(url_for('user'))
    return render_template('login.html')

@app.route('/user', methods=('GET',))
def user():
    if 'user_name' not in session:
        return redirect(url_for('login'))
    user_name = session['user_name']
    return render_template('user.html', usr=user_name)
