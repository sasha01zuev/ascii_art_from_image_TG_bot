from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_data import output_callback

output_type_keyboard = InlineKeyboardMarkup(row_width=1,
                                            inline_keyboard=[
                                                [
                                                    InlineKeyboardButton(text="HTML (Colorized)",
                                                                         callback_data=output_callback.new(
                                                                             type="html")),
                                                    InlineKeyboardButton(text="ASCII (Soon)",
                                                                         callback_data=output_callback.new(
                                                                             type="ascii"))
                                                ]

                                            ]
                                            )
