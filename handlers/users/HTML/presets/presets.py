from aiogram.types import ContentType, ParseMode, InputFile, CallbackQuery
from loader import dp
from keyboards.inline.callback_data import html_customization_callback
from keyboards.inline.html_customization import html_customizations_keyboard
from keyboards.inline.presets import presets_keyboard


@dp.callback_query_handler(html_customization_callback.filter(type='presets'))
async def presets_html(call: CallbackQuery):
    await call.answer(cache_time=3)
    await call.message.delete()
    await call.message.answer('Choose preset:', reply_markup=presets_keyboard)
