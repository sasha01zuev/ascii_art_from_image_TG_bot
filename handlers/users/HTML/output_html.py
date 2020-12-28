from aiogram.types import CallbackQuery
from loader import dp
from keyboards.inline.callback_data import output_callback
from keyboards.inline import html_customizations_keyboard


@dp.callback_query_handler(output_callback.filter(type='html'))
async def customization_html(call: CallbackQuery):
    await call.answer(cache_time=3)
    await call.message.delete()
    await call.message.answer('Select customization for html document:', reply_markup=html_customizations_keyboard)
