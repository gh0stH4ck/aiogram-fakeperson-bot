from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

country_kb = ReplyKeyboardMarkup([
    [
        KeyboardButton(text="Россия"),
        KeyboardButton(text="Украина"),
        KeyboardButton(text="США")
    ]
], resize_keyboard=True)