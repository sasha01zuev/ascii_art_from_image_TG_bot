import os
import shutil

import ascii_magic
import imgkit
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message, InputFile
from loader import dp
from keyboards.inline.callback_data import html_customization_callback
from states import CustomizationHTML
from PIL import Image


@dp.callback_query_handler(html_customization_callback.filter(type='set'))
async def set_html(call: CallbackQuery):
    await call.answer(cache_time=3)
    await call.message.delete()
    await call.message.answer('Write the number of columns (0-1000)')
    await CustomizationHTML.SetSize.set()


@dp.message_handler(state=CustomizationHTML.SetSize)
async def set_columns(message: Message, state: FSMContext):
    await state.update_data(size=message.text)
    data = await state.get_data()
    columns = data.get("size")
    try:  # If user entered digit
        if int(columns) < 0 or int(columns) > 1000:  # If user entered incorrect number
            await message.answer("Chosen default size (135)")
            columns = '135'
            await state.update_data(size=columns)
            await message.answer("Write ratio float (0-10). Or write 'D' for init as default")
            await CustomizationHTML.SetRatio.set()
        else:  # If user entered correct number
            await state.update_data(size=columns)
            await message.answer("Write ratio float (0-10). Or write 'D' for init as default")
            await CustomizationHTML.SetRatio.set()
    except ValueError:  # If user entered characters instead digits
        await message.answer("Chosen default size (135)")
        await message.answer("Write ratio float (0-10). Or write 'D' for init as default")
        columns = '135'
        await state.update_data(size=columns)
        await CustomizationHTML.SetRatio.set()


@dp.message_handler(state=CustomizationHTML.SetRatio)
async def set_ratio(message: Message, state: FSMContext):
    await state.update_data(ratio=message.text)
    username = message.from_user.username
    data = await state.get_data()
    columns = data.get("size")
    ratio = data.get("ratio")
    try:
        if float(ratio) < 0 or float(ratio) > 10:  # If user entered incorrect number
            await message.answer("Chosen default ratio")
            await message.answer('Wait some seconds...')
            output = ascii_magic.from_image_file(f'docs/{username}/picture.png',
                                                 columns=int(columns),
                                                 mode=ascii_magic.Modes.HTML)  # Customization for default html doc
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

            await message.answer('Done! Sending ...')

            if size_mb < 10:  # restriction of Telegram. Image can't be more than 10mb
                await message.answer_photo(InputFile(path_or_bytesio=f'docs/{username}/html.png'))
                await message.answer_document(InputFile(f'docs/{username}/html.png'))
                await message.answer_document(InputFile(f'docs/{username}/ascii.html'))
            else:
                await message.answer('So big size of photo. Sending only photo-document...')
                await message.answer_document(InputFile(f'docs/{username}/html.png'))
                await message.answer_document(InputFile(f'docs/{username}/ascii.html'))

            await message.delete()
            shutil.rmtree(f'docs/{username}/')  # Removing dir with user files

        else:  # If user entered correct number
            await message.answer("Chosen default ratio")
            await message.answer('Wait some seconds...')
            output = ascii_magic.from_image_file(f'docs/{username}/picture.png',
                                                 columns=int(columns), width_ratio=float(ratio),
                                                 mode=ascii_magic.Modes.HTML)  # Customization for default html doc
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

            await message.answer('Done! Sending ...')

            if size_mb < 10:  # restriction of Telegram. Image can't be more than 10mb
                await message.answer_photo(InputFile(path_or_bytesio=f'docs/{username}/html.png'))
                await message.answer_document(InputFile(f'docs/{username}/html.png'))
                await message.answer_document(InputFile(f'docs/{username}/ascii.html'))
            else:
                await message.answer('So big size of photo. Sending only photo-document...')
                await message.answer_document(InputFile(f'docs/{username}/html.png'))
                await message.answer_document(InputFile(f'docs/{username}/ascii.html'))

            await message.delete()
            shutil.rmtree(f'docs/{username}/')  # Removing dir with user files

    except ValueError:  # If user entered characters instead digits
        await message.answer("Chosen default ratio")
        await message.answer('Wait some seconds...')
        output = ascii_magic.from_image_file(f'docs/{username}/picture.png',
                                             columns=int(columns),
                                             mode=ascii_magic.Modes.HTML)  # Customization for default html doc
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

        await message.answer('Done! Sending ...')

        if size_mb < 10:  # restriction of Telegram. Image can't be more than 10mb
            await message.answer_photo(InputFile(path_or_bytesio=f'docs/{username}/html.png'))
            await message.answer_document(InputFile(f'docs/{username}/html.png'))
            await message.answer_document(InputFile(f'docs/{username}/ascii.html'))
        else:
            await message.answer('So big size of photo. Sending only photo-document...')
            await message.answer_document(InputFile(f'docs/{username}/html.png'))
            await message.answer_document(InputFile(f'docs/{username}/ascii.html'))

        await message.delete()
        shutil.rmtree(f'docs/{username}/')  # Removing dir with user files

    await state.finish()
