import asyncio
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from handlers import rout

async def main():
    print('bot started')
    load_dotenv()
    bot = Bot(token=os.getenv('API_TOKEN'))
    dp = Dispatcher()
    dp.include_router(rout)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    print('bot finished')

if __name__ == '__main__':
    asyncio.run(main())