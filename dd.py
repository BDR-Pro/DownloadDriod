import yt_dlp
import requests
from uuid import uuid4
import requests






## youtube

def get_title(video_id):
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
        'skip_download': True,
        'force_generic_extractor': True,
        'force_title': True,
        'force_filename': True,
        'outtmpl': '%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"https://www.youtube.com/watch?v={video_id}", download=False)
        return info.get('title', None)

def download_video(url):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{'key': 'FFmpegVideoConvertor', 'preferedformat': 'mp4'}],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info_dict)

def get_thumbnail(video_id):
    thumb_url= f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
    #download the image
    rsp = requests.get(thumb_url)
    random = uuid4().hex
    file_name = random+".jpg"
    with open(file_name, "wb") as f:
        f.write(rsp.content)
    return file_name

def download_youtube_video(video_id):
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    print("Downloading YouTube video ...")
    path = download_video(video_url)
    print(f"Download complete of {path}.")
    return path


