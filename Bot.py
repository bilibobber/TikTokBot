import asyncio
import logging
import sys
import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from app.handlers.tiktok_handler import tiktok_router
from app.handlers.ai_handler import gpt_router

load_dotenv()

dp = Dispatcher()


async def main() -> None:
    bot = Bot(token=os.getenv('TOKEN'), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp.include_router(gpt_router)
    dp.include_router(tiktok_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        if os.getenv('DEBUG'):
            logging.basicConfig(level=logging.INFO, stream=sys.stdout)

        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
