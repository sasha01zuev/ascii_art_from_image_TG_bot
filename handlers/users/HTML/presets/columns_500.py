import os
import shutil

import ascii_magic
import imgkit
from PIL import Image
from aiogram.types import InputFile, CallbackQuery

from keyboards.inline.callback_data import presets_callback
from loader import dp


@dp.callback_query_handler(presets_callback.filter(size='500_columns'))
async def default_html(call: CallbackQuery):
    """Converting image to html, and taking screenshot of html page"""
    await call.answer(cache_time=3)
    username = call.from_user.username

    await call.message.edit_text('Wait some seconds...')
    output = ascii_magic.from_image_file(f'docs/{username}/picture.png',
                                         columns=500, mode=ascii_magic.Modes.HTML)  # Customization for default html doc
    ascii_magic.to_html_file(f'docs/{username}/ascii.html', output)  # Reversing from image to html

    imgkit.from_file(f'docs/{username}/ascii.html', f'docs/{username}/html.png')  # Screenshot from html page
    ###########################################################################################
    #                                      Cropping Image                                     #
    image = Image.open(f'docs/{username}/html.png')
    width, height = image.size

    # Cropping coordinates
    left = 8
    top = 16
    right = width
    bottom = height - top

    # Cropped image of above dimension
    im = image.crop((left, top, right, bottom))
    # Shows the image in image viewer
    im.save(f'docs/{username}/html.png')
    ###########################################################################################

    size_b = os.path.getsize(f'docs/{username}/html.png')  # Size of screenshot in bytes
    size_mb = size_b / 1_000_000  # Size of screenshot in mb

    await call.message.edit_text('Done! Sending ...')

    if size_mb < 10:  # restriction of Telegram. Image can't be more than 10mb
        await call.message.answer_photo(InputFile(path_or_bytesio=f'docs/{username}/html.png'))
        await call.message.answer_document(InputFile(f'docs/{username}/html.png'))
        await call.message.answer_document(InputFile(f'docs/{username}/ascii.html'))
    else:
        await call.message.answer('So big size of photo. Sending only photo-document...')
        await call.message.answer_document(InputFile(f'docs/{username}/html.png'))
        await call.message.answer_document(InputFile(f'docs/{username}/ascii.html'))

    await call.message.delete()
    shutil.rmtree(f'docs/{username}/')  # Removing dir with user files
