import os.path
from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
import main as mn

app = Flask(__name__, template_folder='templates', static_folder='staticFiles')
app.config['UPLOAD_PATH'] = r'/staticFiles/uploads'


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/', methods=('POST', 'GET'))
def source():
    if request.method == 'POST':
        source_img = request.form['image_file']
        print(source_img.filename)
        img = secure_filename(source_img.filename)
        source_img.save(os.path.join(app.config['UPLOAD_PATH'], img))
        return redirect("/")
        # session['staticFiles/uploads'] = os.path.join(app.config['UPLOAD_FOLDER'], img)


@app.route("/gen")
def generate():
    mn.main()
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)