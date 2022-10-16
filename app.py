import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__, static_url_path='/static')
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
upload_folder = './static/upload'


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(upload_folder, filename))
            saved_image = os.path.join(upload_folder, filename)
            return render_template("index.html", image=saved_image)
    else:
        return render_template("index.html")


@app.route("/result", methods=["GET", "POST"])
def result():
    if request.method == "POST":
        result = request.form["name"]
        return render_template("result.html", result=result)
    else:
        return render_template("result.html")


if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000,
        # ssl_context=()
    )
