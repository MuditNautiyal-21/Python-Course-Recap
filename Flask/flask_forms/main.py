from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def hello_world():
    if(request.method == "POST"):
        # Handling the form
        with open("file.txt", "a") as f:
            f.write(f"{request.form['Name']}: {request.form['Email']}\n")
        return render_template("contact.html")
    else:
        return render_template("contact.html")

app.run(debug=True)