from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="что выведет программа 1")
        ]
    ],
    resize_keyboard=True
)
