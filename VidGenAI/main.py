from flask import Flask, render_template, request
import uuid
import os

from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'user_uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create", methods=["GET", "POST"])
def create():
    myid = uuid.uuid1()
    if request.method == "POST":
        print(request.files.keys())
        rec_id = request.form.get("uuid")
        desc = request.form.get("text")
        input_files = []

        # NEW: ensure per-record folder exists
        rec_dir = os.path.join(app.config['UPLOAD_FOLDER'], rec_id)
        os.makedirs(rec_dir, exist_ok=True)

        for key, value in request.files.items():
            print(key, value)

            # Now we will upload the files:
            file = request.files[key]
            if file:
                filename = secure_filename(file.filename)
                # CHANGED: save into the per-record folder
                file.save(os.path.join(rec_dir, filename))
                input_files.append(filename)

        # writing description ONCE (after file loop)
        if desc:
            with open(os.path.join(rec_dir, "desc.txt"), "a", encoding="utf-8") as f:
                f.write(desc + "\n")

        # writing input.txt in the same folder;
        for fl in input_files:
            with open(os.path.join(rec_dir, "input.txt"), 'a', encoding="utf-8") as f:
                f.write(f"file '{fl}'\n")
                f.write("duration 1\n")

    return render_template("create.html", myid=myid)

@app.route("/gallery")
def gallery():
    reels = os.listdir("static/reels")
    print(reels)
    return render_template("gallery.html", reels=reels)

app.run(debug=True)
