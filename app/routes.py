from app import app
from flask import render_template, send_from_directory
from app.forms import SearchForm
from app.youtube import download
import os

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        video = form.query.data
        # Download video
        filename = download(video)
        # user downloads video/audio
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True, mimetype="audio/mpeg")
    return render_template('index.html', form=form)
