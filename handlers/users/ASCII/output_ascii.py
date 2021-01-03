from aiogram.types import CallbackQuery

from keyboards.inline.callback_data import output_callback
from loader import dp


# If ASCII type was chosen
@dp.callback_query_handler(output_callback.filter(type='ascii'))
async def customization_ascii(call: CallbackQuery):
    await call.answer("Soon!", cache_time=3)
    await call.message.delete()
