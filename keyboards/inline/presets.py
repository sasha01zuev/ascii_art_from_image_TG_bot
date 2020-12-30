from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_data import presets_callback, html_customization_callback

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
                                            ],
                                            [
                                                InlineKeyboardButton(text="135 columns (Default)",
                                                                     callback_data=html_customization_callback.new(
                                                                         type="default"))
                                            ],
                                            [
                                                InlineKeyboardButton(text="200 columns",
                                                                     callback_data=presets_callback.new(
                                                                         size="200_columns"))
                                            ],
                                            [
                                                InlineKeyboardButton(text="300 columns",
                                                                     callback_data=presets_callback.new(
                                                                         size="300_columns"))
                                            ],
                                            [
                                                InlineKeyboardButton(text="400 columns",
                                                                     callback_data=presets_callback.new(
                                                                         size="400_columns"))
                                            ],
                                            [
                                                InlineKeyboardButton(text="500 columns",
                                                                     callback_data=presets_callback.new(
                                                                         size="500_columns"))
                                            ],
                                            [
                                                InlineKeyboardButton(text="600 columns",
                                                                     callback_data=presets_callback.new(
                                                                         size="600_columns"))
                                            ],
                                            [
                                                InlineKeyboardButton(text="700 columns",
                                                                     callback_data=presets_callback.new(
                                                                         size="700_columns"))
                                            ],
                                            [
                                                InlineKeyboardButton(text="1000 columns (slowly)",
                                                                     callback_data=presets_callback.new(
                                                                         size="1000_columns"))
                                            ],
                                            [
                                                InlineKeyboardButton(text="1280 columns (slowly)",
                                                                     callback_data=presets_callback.new(
                                                                         size="1280_columns"))
                                            ]

                                        ]
                                        )
