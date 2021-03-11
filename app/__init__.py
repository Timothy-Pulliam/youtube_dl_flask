from flask import Flask, render_template
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')
app.config['ENVIRONMENT'] = 'development'
app.config['DEBUG'] = True
app.config['UPLOAD_FOLDER'] = os.path.join(basedir, 'uploads')
print(__name__)

from app import routes
