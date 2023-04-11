from flask import Flask, render_template, redirect, url_for

__winc_id__ = "9263bbfddbeb4a0397de231a1e33240a"
__human_name__ = "templates"

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('base.html', title = 'This is my first Flask site')

@app.route("/home")
def home():
    return redirect(url_for('index'))

@app.route("/about")
def about():
    return render_template('about.html', title = 'This about the about')

@app.route("/stuff")
def stuff():
    return render_template('stuff.html', title = 'This is stuff')