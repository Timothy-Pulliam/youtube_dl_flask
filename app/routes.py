from app import app
from flask import render_template, send_from_directory
from app.forms import SearchForm
from app.youtube import download
import os

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    try:
        for item in os.listdir(app.config['UPLOAD_FOLDER']):
            if item.endswith(".mp3"):
                os.remove(os.path.join(app.config['UPLOAD_FOLDER'], item))
    except:
        print("Error deleting old .mp3 files")
    if form.validate_on_submit():
        video = form.query.data
        # Download video
        filename = download(video)
        # user downloads video/audio
        print(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print(os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], filename)))
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True, mimetype="audio/mpeg")
    return render_template('index.html', form=form)
