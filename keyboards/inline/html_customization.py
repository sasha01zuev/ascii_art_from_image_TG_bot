from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_data import html_customization_callback

html_customizations_keyboard = InlineKeyboardMarkup(row_width=1,
                                                    inline_keyboard=[
                                                        [
                                                            InlineKeyboardButton(
                                                                text="Default",
                                                                callback_data=html_customization_callback.new(
                                                                    type="default")),
                                                            InlineKeyboardButton(
                                                                text="Presets",
                                                                callback_data=html_customization_callback.new(
                                                                    type="presets")),
                                                            InlineKeyboardButton(
                                                                text="Set",
                                                                callback_data=html_customization_callback.new(
                                                                    type="set")),
                                                        ]

                                                    ]
                                                    )
