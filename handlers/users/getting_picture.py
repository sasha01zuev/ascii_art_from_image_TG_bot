from aiogram.types import ContentType, Message
from loader import dp
from utils.misc import rate_limit


@rate_limit(limit=5)  #anti-spam
@dp.message_handler(content_types=ContentType.PHOTO)
async def getting_photo(message: Message):
    """Downloading to directory picture from message. Selecting background color from pic"""
    try:
        await message.photo[-1].download('pictures/picture.png')
        await message.answer("Choose background color:")
    except Exception as err:
        await message.answer(f'Oops, some unknown error\n{err}')
