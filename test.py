from aiogram.dispatcher.filters.state import State, StatesGroup
from math import ceil


class Test(StatesGroup):
    question = State()
    counter = 0
    quantity = 0
    goodAnswers = 0
    rightAnswer = 0
    mode = 0

    def result(self):
        result = f"Ты ответел правильно на {self.goodAnswers}"

        if self.goodAnswers % 100 >= 10 and self.goodAnswers <= 20 or self.goodAnswers % 10 == 5:
            result += " вопросов "
        elif self.goodAnswers % 10 == 1:
            result += " вопрос "
        else:
            result += " вопроса "

        rating = ceil(self.goodAnswers / self.quantity * 5)
        if rating < 2:
            rating = 2
        result += f"\nи получил оценку {int(rating)}. "
        string_array = ("Не расстраивайся. Математика дана не всем",
                        "Не расстраивайся. Математика дана не всем", "Ты можешь лучше",
                        "Неплохой результат",
                        "Умница")
        result += string_array[rating-1]
        return result
