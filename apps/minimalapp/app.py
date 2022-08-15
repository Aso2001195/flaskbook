from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Helo,Flaskbook!"


@app.route('/hello')
def hello():
    return "Hello, World!"
