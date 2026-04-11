import asyncio
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

from db import init_db
from handlers import rout

async def main():
    print('bot started')
    load_dotenv()
    init_db()
    bot = Bot(token=os.getenv('API_TOKEN'))
    dp = Dispatcher()
    dp.include_router(rout)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    print('bot finished')

if __name__ == '__main__':
    asyncio.run(main())