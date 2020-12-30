from aiogram.types import ContentType, Message, ParseMode, InputFile
from loader import dp
from utils.misc import rate_limit
from keyboards.inline import output_type_keyboard
import os


@rate_limit(limit=10)  # anti-spam
@dp.message_handler(content_types=ContentType.PHOTO)
async def getting_photo(message: Message):
    """Downloading to user directory picture from message."""
    username = message.from_user.username
    try: # If dir is not exist
        os.mkdir(f'docs/{username}')
    except: # If dir exist
        print('Dir exist')

    await message.photo[-1].download(f'docs/{username}/picture.png')  # Downloading image to directory of user
    await message.answer('Select type of output:', reply_markup=output_type_keyboard)


