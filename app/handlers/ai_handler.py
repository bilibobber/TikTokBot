from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from app.scripts.openai_query import gpt_answer

gpt_router = Router()


@gpt_router.message(Command('gpt'))
async def ai_answer(message: Message):
    loading_msg = await message.answer('Думаю🔄')

    try:
        await message.answer(gpt_answer(message.text[3:]))
    except Exception as e:
        await message.reply('❌Ошибка!')
        print(f'Ошибка обработки (ai): {e}')

    await loading_msg.delete()
