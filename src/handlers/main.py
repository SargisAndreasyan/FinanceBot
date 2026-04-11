from aiogram import Router, types
from aiogram.filters import Command
from services import UserService
from .categories import ctg
rout = Router()
rout.include_router(ctg)

@rout.message(Command('start'))
async def start_handler(message: types.Message):
    us = UserService()
    answer = us.create_user(t_id=message.from_user.id)
    print(answer)
    await message.answer('Hello I am your finance bot')