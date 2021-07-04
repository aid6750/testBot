from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Проверить навык сложения")
        ],
        [
            KeyboardButton(text="Проверить навык умножения")
        ]
    ],
    resize_keyboard=True
)

proposals = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="5")
        ],
        [
            KeyboardButton(text="10")
        ],
        [
            KeyboardButton(text="15")
        ],
        [
            KeyboardButton(text="20")
        ],
    ],
    resize_keyboard=True
)
