from main import dp, bot
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher.filters import Command, Text
from menu import menu, proposals
from test import Test
from random import randrange
from aiogram.dispatcher import FSMContext
from contextvars import ContextVar
from config import ADMIN_ID
from math import ceil

test = Test()


@dp.message_handler(Command("test"))
async def enter_test(message: Message):
    await message.answer(text="Выберите испытание", reply_markup=menu)


@dp.message_handler(Text(equals=["Проверить навык сложения", "Проверить навык умножения"]))
async def on_button_menu_clicked(message: Message):
    global test
    if message.text == "Проверить навык сложения":
        test.mode = "+"
    else:
        test.mode = "*"

    await message.answer(f'Сколько примеров вы хотите решить?', reply_markup=proposals)


@dp.message_handler(Text(equals=["5", "10", "15", "20"]))
async def on_button_proposals_clicked(message: Message):
    global test
    quantity = int(message.text)
    await message.answer(f"желаю удачи, {message.from_user.username}")
    test.quantity = quantity
    operand1 = randrange(100)
    operand2 = randrange(100)
    question = f"сколько будет {operand1}{test.mode}{operand2}?"

    if test.mode == "*":
        test.rightAnswer = operand1 * operand2
    else:
        test.rightAnswer = operand1 + operand2

    test.quantity = quantity
    await message.answer(text=question, reply_markup=ReplyKeyboardRemove())
    await test.question.set()


@dp.message_handler(state=Test.question)
async def answer(message: Message, state: FSMContext):
    global test
    praise = ("молодец", "так держать!", "здорово", "Ты просто монстр", "Продолжай в том же духе")
    test.counter += 1
    if test.counter <= test.quantity:
        number = 0
        try:
            number = int(message.text)
        except BaseException:
            await message.answer("введите число")
            return

        if number == test.rightAnswer:
            await message.answer(praise[randrange(len(praise))])
            test.goodAnswers += 1
        else:
            await message.answer("не верно")
    if test.quantity != test.counter:
        op1 = randrange(100)
        op2 = randrange(100)
        ques = f"сколько будет {op1}{test.mode}{op2}?"

        if test.mode == "*":
            test.rightAnswer = op1 * op2
        else:
            test.rightAnswer = op1 + op2

        await message.answer(text=ques)
        await test.question.set()
    if test.counter == test.quantity:
        await message.answer(test.result())
        await state.finish()
        test.counter = 0
        await bot.send_message(chat_id=ADMIN_ID, text=f"пользователь {message.from_user.username} "
                                                      f"получил оценку {test.rating}")


