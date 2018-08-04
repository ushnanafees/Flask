from flask import Flask

app = Flask(__name__)

@app.route("/user/<name>")

def index(name):
    return "Hello dear : " + name.title()

app.run(debug = True, use_reloader = False)