from aiogram.filters import Command
from aiogram import Router, types
from services import CategoryService

ctg = Router()

from aiogram.filters import Command
from aiogram import types

@ctg.message(Command("create_category"))
async def create_category(message: types.Message):
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        await message.answer("Usage: /create_category <name>")
        return
    category_name = args[1]
    cs = CategoryService(message.from_user.id)
    cs.create_category(category_name)

    await message.answer(f"Category '{category_name}' created")


@ctg.message(Command("remove_category"))
async def remove_category(message: types.Message):
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        await message.answer("Usage: /delete_category <name>")
        return
    category_name = args[1]
    cs = CategoryService(message.from_user.id)
    cs.delete_category(category_name)

    await message.answer(f"Category '{category_name}' deleted")

@ctg.message(Command("edit_category"))
async def edit_category(message: types.Message):
    args = message.text.split(maxsplit=2)

    if len(args) < 3:
        await message.answer("Usage: /edit_category <old_name> <new_name>")
        return

    old_name = args[1]
    new_name = args[2]

    cs = CategoryService(message.from_user.id)
    result = cs.edit_category(old_name, new_name)

    await message.answer(result)
