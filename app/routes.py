from app import app
from flask import render_template, send_from_directory
from app.forms import SearchForm
import youtube_dl
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


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

def download(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'logger': MyLogger(),
        'progress_hooks': [my_hook],
        'outtmpl': app.config['UPLOAD_FOLDER'] + '/%(title)s-%(id)s.%(ext)s',
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    info = ydl.extract_info(url, download=False)
    title = info['title']
    id = info['id']
    ext = info['ext']
    return title + '-' + id + '.mp3'


if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=VN5kzHnqOCE"
    download(url)
