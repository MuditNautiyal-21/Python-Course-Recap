from flask import Flask, flash, render_template, redirect

app = Flask(__name__)

app.secret_key = "somesuper_secretkey_couldberandom"

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/logout")
def logout():
    flash("you have been logged out!", "success")
    return render_template('logout.html')

app.run(debug=True)