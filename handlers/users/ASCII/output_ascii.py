import os
import shutil

from aiogram.types import CallbackQuery, InputFile

from keyboards.inline.callback_data import output_callback
from loader import dp
import ascii_magic
import imgkit


# If ASCII type was chosen
@dp.callback_query_handler(output_callback.filter(type='ascii'))
async def customization_ascii(call: CallbackQuery):
    await call.answer(cache_time=3)
    username = call.from_user.username
    await call.message.edit_text('Wait some seconds...')

    # Customization for default ascii
    output = ascii_magic.from_image_file(f'docs/{username}/picture.png', columns=129, mode=ascii_magic.Modes.ASCII)

    with open(f'docs/{username}/ascii.txt', "w") as f:
        f.write(output)

    # txt to to png
    imgkit.from_file(f'docs/{username}/ascii.txt', f'docs/{username}/ascii.png')

    await call.message.edit_text('Done! Sending ...')

    size_b = os.path.getsize(f'docs/{username}/ascii.png')  # Size of screenshot in bytes
    size_mb = size_b / 1_000_000  # Size of screenshot in mb

    if size_mb < 10:  # restriction of Telegram. Image can't be more than 10mb
        await call.message.answer_photo(InputFile(path_or_bytesio=f'docs/{username}/ascii.png'))
        await call.message.answer_document(InputFile(f'docs/{username}/ascii.png'))
        await call.message.answer_document(InputFile(f'docs/{username}/ascii.txt'))
    else:
        await call.message.answer('So big size of photo. Sending only photo-file...')
        await call.message.answer_document(InputFile(f'docs/{username}/ascii.png'))
        await call.message.answer_document(InputFile(f'docs/{username}/ascii.txt'))

    await call.message.delete()
    shutil.rmtree(f'docs/{username}/')  # Removing dir with user files
