from aiogram import Router, F
from aiogram.types import Message, InputMediaPhoto, FSInputFile

from app.scripts.tiktok_url_extractor import get_tiktok_video_url
from app.scripts.youtube_video_downloader import download_youtube_video

upload_router = Router()

TIKTOK_URL_PATTERN = r'(https?://)?(www\.|v[mt]\.)?tiktok\.com/'
YOUTUBE_URL_PATTERN = r'(https?://)?(www\.|m\.)?(youtube\.com|youtu\.be)(-nocookie)?/'


def create_urls_list(message: Message):
    if message.entities:
        urls = [
            message.text[e.offset: e.offset + e.length]
            for e in message.entities
            if e.type == "url"
        ]

        return urls


@upload_router.message(F.chat.type.in_({"private", "group", "supergroup"}), F.text.regexp(TIKTOK_URL_PATTERN))
async def handle_tiktok_videos(message: Message):
    urls = create_urls_list(message)

    if not urls:
        await message.reply('❌Ошибка загрузки')
        return

    for url in urls:
        response_type, response_content = get_tiktok_video_url(url)
        print(response_content)
        if response_type:
            loading_msg = await message.answer('Видео загружается🔄')

            if response_type == 'url':
                try:
                    await message.reply_video(
                        video=response_content,
                        supports_streaming=True
                    )
                except Exception as e:
                    await message.reply('❌Ошибка!')
                    print(f'Ошибка обработки (tiktok_url): {e}')

            elif response_type == 'img':
                try:
                    media = [InputMediaPhoto(media=img) for img in response_content]
                    await message.reply_media_group(media=media,
                                                    )
                except Exception as e:
                    await message.reply('❌Ошибка!')
                    print(f'Ошибка обработки (tiktok_img): {e}')

            await loading_msg.delete()
        else:
            await message.reply('❌Ошибка загрузки')


@upload_router.message(F.chat.type.in_({"private", "group", "supergroup"}), F.text.regexp(YOUTUBE_URL_PATTERN))
async def handle_youtube_videos(message: Message):
    urls = create_urls_list(message)

    if not urls:
        await message.reply('❌Ошибка загрузки')
        return

    for url in urls:
        loading_msg = await message.answer('Видео загружается🔄')
        success = download_youtube_video(url)

        if not success:
            await message.reply('❌Ошибка!')
            return

        try:
            # Чтобы передать локальный файл в reply_video(video=), нужно использовать FSInputFile

            await message.reply_video(
                video=FSInputFile('temp/temp.mp4'),
                supports_streaming=True,
            )
        except Exception as e:
            await message.reply('❌Ошибка!')
            print(f'Ошибка обработки (youtube_url): {e}')

        await loading_msg.delete()


