from aiogram.dispatcher.filters.state import StatesGroup, State


# Example:
# class Start(StatesGroup):
#     SetStartCommand = State()


class CustomizationHTML(StatesGroup):
    SetSize = State()
    SetRatio = State()


class CustomizationASCII(StatesGroup):
    SetSize = State()
