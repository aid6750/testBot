from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="верхняя кнопка")
        ],
        [
            KeyboardButton(text="нижняя кнопка 1"),
            KeyboardButton(text="нижняя кнопка 2")
        ]
    ],
    resize_keyboard=True
)
