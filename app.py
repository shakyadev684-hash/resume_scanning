from flask import Flask, render_template, request
import os
from utils import process_resume

app = Flask(__name__)
UPLOAD_FOLDER = "resumes"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# create folder if not exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["resume"]
    job_description = request.form["job_description"]

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    score = process_resume(filepath, job_description)

    return render_template("result.html", score=score)

if __name__ == "__main__":
    app.run(debug=True)