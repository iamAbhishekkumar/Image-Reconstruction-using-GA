from main import pipleline
from flask import Flask, Response, render_template, request, redirect, url_for
from src.constants import IMG_PATH
app = Flask(__name__)


SHAPE = None
current_frame = 0


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process_image', methods=['POST'])
def process_image():
    global SHAPE
    image = request.files['image']
    SHAPE = request.form['shape']
    image.save(IMG_PATH)
    return redirect('/preview_feed')


@app.route('/preview_feed')
def preview_feed():
    return Response(pipleline(IMG_PATH, SHAPE), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(debug=True)
