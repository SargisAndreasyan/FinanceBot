from aiogram import Router, types
from aiogram.filters import Command

rout = Router()

@rout.message(Command('start'))
async def start_handler(message: types.Message):
    await message.answer('Hello I am your finance bot')