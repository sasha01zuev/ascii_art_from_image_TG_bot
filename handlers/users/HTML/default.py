import ascii_magic
import imgkit
import os, shutil
from aiogram.types import InputFile, CallbackQuery
from loader import dp
from keyboards.inline.callback_data import html_customization_callback


@dp.callback_query_handler(html_customization_callback.filter(type='default'))
async def default_html(call: CallbackQuery):
    await call.answer(cache_time=3)
    # await call.message.delete()
    username = call.from_user.username

    await call.message.edit_text('Wait some seconds...')
    output = ascii_magic.from_image_file(f'docs/{username}/picture.png',
                                         columns=135, mode=ascii_magic.Modes.HTML)
    ascii_magic.to_html_file(f'docs/{username}/ascii.html', output)

    imgkit.from_file(f'docs/{username}/ascii.html', f'docs/{username}/html.png')
    size_b = os.path.getsize(f'docs/{username}/html.png')
    size_mb = size_b / 1_000_000

    await call.message.edit_text('Done! Sending ...')

    if size_mb < 10:
        await call.message.answer_photo(InputFile(path_or_bytesio=f'docs/{username}/html.png'))
        await call.message.answer_document(InputFile(f'docs/{username}/html.png'))
        await call.message.answer_document(InputFile(f'docs/{username}/ascii.html'))
    else:
        await call.message.answer('So big size of photo. Sending only photo-document...')
        await call.message.answer_document(InputFile(f'docs/{username}/html.png'))
        await call.message.answer_document(InputFile(f'docs/{username}/ascii.html'))

    await call.message.delete()
    shutil.rmtree(f'docs/{username}/')
