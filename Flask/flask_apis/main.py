from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def json():
    marks = {
    "Jack": 85,
    "Jill": 90,
    "John": 78,
    "Jane": 92,
    "Jim": 88
}
    values= [1, marks, 67]
    return jsonify(values)

app.run(debug=True)