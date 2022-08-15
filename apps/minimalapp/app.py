from flask import Flask, current_app, g, render_template, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return "Helo,Flaskbook!"


@app.route("/hello/<name>", methods=['GET'], endpoint='hello-endpoint')
def hello(name):
    return f"Hello, {name}!"


@app.route("/name/<name>")
def show_name(name):
    return render_template("index.html", name=name)


with app.test_request_context():
    print(url_for("index"))
    print(url_for("hello-endpoint", name="world"))
    print(url_for("show_name", name="ichiro", page="1"))


ctx = app.app_context()
ctx.push()

print(current_app.name)

g.connection = "connection"
print(g.connection)
