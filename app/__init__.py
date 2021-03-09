from flask import Flask, render_template
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = '0q90j0fsjJAAAOF90283428300fiojfASDFQTaS'
app.config['UPLOAD_FOLDER'] = os.path.join(basedir, 'uploads')
print(basedir)
print(app.config['UPLOAD_FOLDER'])

from app import routes
