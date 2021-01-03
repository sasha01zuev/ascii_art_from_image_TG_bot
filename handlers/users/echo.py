from aiogram import types

from loader import dp


@dp.message_handler()
async def echo(message: types.Message):
    """Answer for simple message"""
    await message.answer("I work with pictures only🤫")
