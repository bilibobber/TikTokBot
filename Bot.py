import asyncio
import logging
import sys
import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from app.handlers.upload_handlers import upload_router
from app.handlers.ai_handler import gpt_router

load_dotenv()

dp = Dispatcher()


async def main() -> None:
    bot = Bot(token=os.getenv('TOKEN'), default=DefaultBotProperties(parse_mode="HTML", file_upload_limit=100 * 1024 * 1024))
    dp.include_router(gpt_router)
    dp.include_router(upload_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        if os.getenv('DEBUG'):
            logging.basicConfig(level=logging.INFO, stream=sys.stdout)

        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")

'''
import yt_dlp


def get_video_youtube_url(url):
    try:
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'quiet': True,
            'no_warnings': True,
            'simulate': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)  # .extract_info - получить прямую ссылку на видео
            return info['url']
    except Exception as e:
        print(f"Ошибка (get_youtube_video_url): {e}")
        return False

print(get_video_youtube_url('https://www.youtube.com/shorts/yLlzJtSMHwg?feature=share'))

'''