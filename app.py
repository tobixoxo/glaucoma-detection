# app.py
from flask import Flask, flash, request, redirect, url_for, render_template
import urllib.request
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads/'

app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

counter = 0

def count_up():
    global counter
    counter = counter + 1
    return str(counter)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def upload_image():
    # first 2 if statements describe cases where file not uploaded
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    # file variable is a file handler for the uploaded file present in the request object
    file = request.files['file']

    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)

    # actual upload code
    if file and allowed_file(file.filename):
        # configure image name before storing
        actualfilename = secure_filename(file.filename)
        actualfilename_array = actualfilename.rsplit('.')

        extension = actualfilename_array[-1]
        saved_file_name_prefix = "Input_Image_" + count_up()

        file.save(os.path.join(
            app.config['UPLOAD_FOLDER'], saved_file_name_prefix + '.' + extension))

        #print('upload_image filename: ' + filename)
        flash('Image successfully uploaded and displayed below')
        return render_template('index.html', filename=saved_file_name_prefix + '.' + extension)
    else:
        flash('Allowed image types are - png,jpeg')
        return redirect(request.url)

@app.route('/display/<filename>')
def display_image(filename):
    #print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

@app.route('/about')
def desc():
    return render_template('aboutus.html')

if __name__ == "__main__":
    app.run()
