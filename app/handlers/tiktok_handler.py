import time
import random

from aiogram import Router, F
from aiogram.types import Message, InputMediaPhoto

from app.scripts.download_url_creator import get_download_url

tiktok_router = Router()


@tiktok_router.message(F.chat.type.in_({"private", "group", "supergroup"}))
async def handle_all_messages(message: Message):
    if not message.text:
        return

    if message.entities:
        urls = [
            message.text[e.offset: e.offset + e.length]
            for e in message.entities
            if e.type == "url"
        ]
        if urls:
            tiktok_urls = [url for url in urls if
                           url[0:22] == 'https://vt.tiktok.com/' or url[0:22] == 'https://vm.tiktok.com/' or url[
                                                                                                             0:23] == 'https://www.tiktok.com/']
            for url in tiktok_urls:
                time.sleep(1.1)
                response_type, response_content = get_download_url(url)
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
                            print(f'Ошибка обработки (url): {e}')
                    elif response_type == 'img':
                        try:
                            media = [InputMediaPhoto(media=img) for img in response_content]
                            await message.reply_media_group(media=media,
                                                            )
                        except Exception as e:
                            await message.reply('❌Ошибка!')
                            print(f'Ошибка обработки (img): {e}')

                    await loading_msg.delete()
                else:
                    await message.reply('❌Ошибка загрузки')

