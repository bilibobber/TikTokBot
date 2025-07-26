import os

import yt_dlp

from dotenv import load_dotenv

load_dotenv()

if os.getenv('DEBUG'):
    ydl_opts = {
        'format': 'best[ext=mp4]',
        'outtmpl': 'temp/temp.mp4',
        'overwrites': True,
        'quiet': True,
        'no_warnings': True,
        'no_call_home': True,
        'no_color': True,
        'no_progress': True,
        'noprogress': True,
        'logger': None,
        'progress_hooks': [],
        'verbose': False
    }
else:
    ydl_opts = {
        'format': 'best[ext=mp4]',
        'outtmpl': 'temp/temp.mp4',
        'overwrites': True
    }


def download_youtube_video(url):
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(url)
            return True

    except Exception as e:
        print(f'Ошибка (get_youtube_video_url): {e}')
        return False
