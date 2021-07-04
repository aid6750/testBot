from main import dp
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher.filters import Command, Text
from menu import menu


@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer(text="нажмите любую кнопку", reply_markup=menu)


@dp.message_handler(Text(equals=["верхняя кнопка", "нижняя кнопка 1", "нижняя кнопка 2"]))
async def on_button_menu_clicked(message: Message):
    print(ReplyKeyboardRemove())
    await message.answer(f'вы выбрали "{message.text}"', reply_markup=ReplyKeyboardRemove())


@dp.message_handler()
async def answer_to_message(message : Message):
    await message.answer("Я тут")