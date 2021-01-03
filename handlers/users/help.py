from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from loader import dp
from utils.misc import rate_limit


@rate_limit(limit=5)  # Anti-spam
@dp.message_handler(Command("help"))
async def start(message: Message):
    await message.answer("Send me picture and choose type of output art image\n"
                         "    ✅ If you chosen ASCII, there are only default customization\n"
                         "    ✅ If you chosen HTML, there are 3 kinds of customization. You can try every\n"
                         "    ✅ As a result, you will receive a picture, a picture file and a document file with art\n"
                         "    ✅ If output image more than 10 MB then only the files will be sent\n"
                         "    ✅ If you configure the output of the image yourself, the image will not be cropped!")
