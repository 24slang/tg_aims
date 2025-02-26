import asyncio

from aiogram import Bot

from handlers import dp
from config import BOT_TOKEN


async def main():
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
