from aiogram.filters import Command
from aiogram import Router, types

ctg = Router()

@ctg.message(Command('create_category'))
async def create_category(message: types.Message):
    print('Here will be created category')

@ctg.message(Command("remove_category"))
async def remove_category(message: types.Message):
    print('Here will be removed category')

@ctg.message(Command("edit_category"))
async def edit_category(message: types.Message):
    print('Here will be edited category')
