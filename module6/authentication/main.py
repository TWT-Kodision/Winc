import os

from flask import Flask, redirect, render_template, request, session, url_for
from helpers import valid_password
__winc_id__ = "8fd255f5fe5e40dcb1995184eaa26116"
__human_name__ = "authentication"

app = Flask(__name__)

app.secret_key = os.urandom(16)


@app.route("/home")
def redirect_index():
    return redirect(url_for("index"))


@app.route("/")
def index():
    return render_template("index.html", title="Index")


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/lon")
def lon():
    return render_template("lon.html", title="League of Nations")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        if valid_password(request.form['username'], request.form['password']):
            session['logged'] = True
            session['username']= request.form['username']
            return redirect(url_for('dashboard'))
        return redirect(url_for('login', error=True))
    return render_template("login.html", title="login")
      

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", title="dashboard")


@app.route("/logout", methods=["GET", "POST"])
def logout():
    session['logged'] = False
    session.pop('username', None)
    return redirect(url_for('index'))


app.run