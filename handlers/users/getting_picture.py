from aiogram.types import ContentType, Message, ParseMode, InputFile
from loader import dp
from utils.misc import rate_limit
from keyboards.inline import output_type_keyboard


@rate_limit(limit=5)  # anti-spam
@dp.message_handler(content_types=ContentType.PHOTO)
async def getting_photo(message: Message):
    """Downloading to directory picture from message."""
    await message.photo[-1].download('pictures/picture.png')
    await message.answer('Select type of output:', reply_markup=output_type_keyboard)


