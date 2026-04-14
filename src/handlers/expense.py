from aiogram import Router, F
from aiogram.types import Message

exp = Router()

def parse_spent(text: str):
    parts = text.split()
    if len(parts) < 2:
        return None, None, None
    category = parts[0]
    amount = parts[1]
    description = " ".join(parts[2:]) if len(parts) > 2 else ""
    return category, amount, description

@exp.message(F.text)
async def handle_spent(message: Message):
    category, amount, description = parse_spent(message.text)
    await message.answer(f"""{category}, 
{amount}, 
{description}""")

