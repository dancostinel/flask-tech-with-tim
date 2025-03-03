from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/<name>')
def hello(name):
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
