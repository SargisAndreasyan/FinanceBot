import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart

bot = Bot(token=os.getenv('API_TOKEN'))
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer('First message')


async def main():
    print('bot started')
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    print('bot finished')

if __name__ == '__main__':
    asyncio.run(main())