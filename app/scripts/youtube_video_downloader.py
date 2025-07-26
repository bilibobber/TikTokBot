import yt_dlp

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
