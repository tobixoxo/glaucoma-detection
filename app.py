import os
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/uploaded_images'
ALLOWED_EXTENSIONS = {'png'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'super secret key'


@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')
# main driver functions
if __name__ == '__main__':
    app.run()
