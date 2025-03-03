from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/<name>')
def hello(name):
    return render_template('index.html', name=name)
