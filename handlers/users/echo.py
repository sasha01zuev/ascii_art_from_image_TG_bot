from aiogram import types

from data.config import MAIN_ADMIN
from loader import dp, bot
from utils.misc import rate_limit


@rate_limit(limit=10)  # anti-spam
@dp.message_handler()
async def echo(message: types.Message):
    """Answer for simple message"""
    await message.answer("I work with pictures only🤫")
    message_text = message.text
    await bot.send_message(MAIN_ADMIN, message_text)
