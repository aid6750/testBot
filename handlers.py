from main import dp, bot
from aiogram.types import Message
from aiogram.dispatcher.filters import Command, Text
from menu import menu
from test import Test
from random import randrange
from aiogram.dispatcher import FSMContext
from config import ADMIN_ID
import time


@dp.message_handler(Command("test"), state=None)
async def enter_test(message: Message):
    await message.answer(text="Выберите испытание", reply_markup=menu)


@dp.message_handler(Text(equals=["что выведет программа 1"]))
async def on_button_menu_clicked(message: Message, state: FSMContext):
    test = Test()
    test.counter = 0
    test.mode = message.text
    test.quantity = len(test.tests[message.text])
    await state.update_data({"test": test})
    question = open(test.tests[test.mode][test.counter + 1][0], "rb")
    intro = test.tests[test.mode][test.counter+1][3]
    await message.answer(intro)
    time.sleep(3)
    await bot.send_photo(chat_id=message.chat.id, photo=question)
    await test.question.set()


@dp.message_handler(state=Test.question)
async def answer(message: Message, state: FSMContext):
    test = await state.get_data()
    test = test.get("test")
    praise = ("молодец", "так держать!", "здорово", "правильно!", "верно, продолжай в том же духе")
    rightAnswer = test.tests[test.mode][test.counter + 1][1].lower().strip()
    explanation = test.tests[test.mode][test.counter + 1][2]

    if message.text.lower().strip() != rightAnswer:
        await message.answer("не верно")
        await message.answer(explanation)
    else:
        await message.answer(praise[randrange(len(praise))])
        test.goodAnswers += 1
    test.counter += 1
    await state.update_data({"test": test})
    if test.quantity > test.counter:
        await test.question.set()
        question = open(test.tests[test.mode][test.counter + 1][0], "rb")
        await bot.send_photo(chat_id=message.chat.id, photo=question)
    if test.counter == test.quantity:
        await message.answer(test.result())
        await state.update_data({"test": Test()})
        await state.finish()
        await bot.send_message(chat_id=ADMIN_ID, text=f"пользователь {message.from_user.username} "
                                                      f"получил оценку {test.rating}")


@dp.message_handler()
async def undefined_message(message: Message):
    await message.answer("я вас не понимаю. Для запуска бота введите команду /test")
