from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

gender_select = ReplyKeyboardMarkup([
    [KeyboardButton("Женский"), KeyboardButton("Мужской")]
], resize_keyboard=True)