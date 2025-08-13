from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    marks={
        "John": 85,
        "Jane": 90,
        "Doe": 78,
        "Alice": 92,
        "Bob": 88,
        "Lilly": 53
    }
    return render_template("index.html", marks=marks)

app.run(debug=True)