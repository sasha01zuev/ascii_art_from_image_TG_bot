from aiogram.types import ContentType, Message, ParseMode, InputFile
from loader import dp
from utils.misc import rate_limit


@rate_limit(limit=5)  # anti-spam
@dp.message_handler(content_types=ContentType.PHOTO)
async def getting_photo(message: Message):
    """Downloading to directory picture from message."""
    await message.photo[-1].download('pictures/picture.png')


