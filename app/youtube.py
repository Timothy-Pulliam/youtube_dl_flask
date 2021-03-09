from app import app
import youtube_dl

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

def my_hook(d):
    if d['status'] == 'downloading':
        print("""status: downloading
        download speed: {}
        eta: {}
        percent: {}
        """.format(d['_speed_str'], d['_eta_str'], d['_percent_str']))
    if d['status'] == 'finished':
        print("""status: finished downloading
        file size: {}
        """.format(d['_total_bytes_str']))
        print('Done downloading, now converting to mp3...')

def download(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        # max file size in bytes (100MB)
        'max_filesize': 100000000,
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

if __name__ == '__main__':
    url = "https://www.youtube.com/watch?v=VN5kzHnqOCE"
    download(url)
