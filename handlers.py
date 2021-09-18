from aiogram.types.base import InputFile
from main import dp, bot
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher.filters import Command, Text, state
from menu import menu
from test import Test
from random import randrange
from aiogram.dispatcher import FSMContext
from config import ADMIN_ID
from aiogram.types import InputFile
test = Test()
import time

@dp.message_handler(Command("test"),state = None)
async def enter_test(message: Message):
    await message.answer("""вам будет предложена серия вопросов. Каждый вопрос представляет собой картинкус кодом. Вы должны понять, что выведет данная программа.
    дробные ответы нужно округлять до сотых
    error - ошибка компиляции
    UB - поведение программы не определено
    желаю удачи
    """)
    await message.answer(text="Выберите испытание", reply_markup=menu)


@dp.message_handler(Text(equals=["тест 1"]))
async def on_button_menu_clicked(message: Message, state : FSMContext):
    test = Test()
    test.counter = 0
    test.mode = message.text
    test.quantity = len(test.tests[message.text])
    await state.update_data({"test": test})
    question=open(test.tests[test.mode][test.counter+1][0],"rb");
    await bot.send_photo(chat_id=message.chat.id, photo=question)
    await test.question.set()



@dp.message_handler(state=Test.question)
async def answer(message: Message, state: FSMContext):
    test = await state.get_data()
    test = test.get("test")
    praise = ("молодец", "так держать!", "здорово", "правильно!", "верно, продолжай в том же духе")
    rightAnswer = test.tests[test.mode][test.counter+1][1]
    explanation = test.tests[test.mode][test.counter+1][2]

    if(message.text.lower() == rightAnswer.lower()):
        await message.answer(praise[randrange(len(praise))])
        test.goodAnswers += 1
    else:
        await message.answer("не верно")
        await message.answer(explanation)
    test.counter += 1
    await state.update_data({"test":test})
    if test.quantity > test.counter:
        await test.question.set()
        question=open(test.tests[test.mode][test.counter+1][0],"rb");
        await bot.send_photo(chat_id=message.chat.id, photo=question)
    if test.counter == test.quantity:
        await message.answer(test.result())
        await state.update_data({"test": Test()})
        await state.finish()
        await bot.send_message(chat_id=ADMIN_ID, text=f"пользователь {message.from_user.username} "
                                                      f"получил оценку {test.rating}")
