from flask import Flask, render_template, \
url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/about")
def second():
    return render_template('second.html')

app.run(debug = True, use_reloader = True, port = 3000)


#NOTE: view function name r file name same hona chaiye must jo render karwa rahe wrna error ayga