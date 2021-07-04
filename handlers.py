from main import dp
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher.filters import Command, Text
from menu import menu, proposals
from test import Test
from random import randrange


@dp.message_handler(Command("test"))
async def enter_test(message: Message):
    praise = ("молодец", "так держать!", "здорово", "Ты просто монстр", "Продолжай в том же духе")
    await message.answer(text="Выберите испытание", reply_markup=menu)

    @dp.message_handler(Text(equals=["Проверить навык сложения", "Проверить навык умножения"]))
    async def on_button_menu_clicked(mode: Message):
        if mode.text == "Проверить навык сложения":
            mode = "+"
        else:
            mode = "*"
        await message.answer(f'Сколько примеров вы хотите решить?', reply_markup=proposals)

        @dp.message_handler(Text(equals=["5", "10", "15", "20"]))
        async def on_button_proposals_clicked(quantity: Message):
            quantity = int(quantity.text)
            await message.answer(f"желаю удачи, {message.from_user.username}")
            test = Test(quantity)
            operand1 = randrange(100)
            operand2 = randrange(100)
            question = f"сколько будет {operand1}{mode}{operand2}?"

            if mode == "*":
                test.rightAnswer = operand1 * operand2
            else:
                test.rightAnswer = operand1 + operand2

            await message.answer(text=question, reply_markup=ReplyKeyboardRemove())
            await test.question.set()

            @dp.message_handler(state=Test.question)
            async def answer(ans: Message):
                number = 0
                try:
                    number = int(ans.text)
                except BaseException:
                    await message.answer("введите число")
                    await test.question.set()
                    return

                test.counter += 1
                if number == test.rightAnswer:
                    await message.answer(praise[randrange(len(praise))])
                    test.goodAnswers += 1
                else:
                    await message.answer("не верно")

                if test.counter < test.quantity:
                    op1 = randrange(100)
                    op2 = randrange(100)
                    ques = f"сколько будет {op1}{mode}{op2}?"

                    if mode == "*":
                        test.rightAnswer = op1 * op2
                    else:
                        test.rightAnswer = op1 + op2

                    await message.answer(text=ques)
                    await test.question.set()
                else:
                    await message.answer(test.result())
