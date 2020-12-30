from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_data import presets_callback

presets_keyboard = InlineKeyboardMarkup(row_width=1,
                                        inline_keyboard=[
                                            [
                                                InlineKeyboardButton(text="50 columns",
                                                                     callback_data=presets_callback.new(
                                                                         size="50_columns"))
                                            ],
                                            [
                                                InlineKeyboardButton(text="100 columns",
                                                                     callback_data=presets_callback.new(
                                                                         size="100_columns"))
                                            ]

                                        ]
                                        )
