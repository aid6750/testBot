from aiogram.dispatcher.filters.state import State, StatesGroup
from math import ceil
from aiogram.types import InputFile

class Test(StatesGroup):
    question = State()
    counter = 0
    quantity = 0
    goodAnswers = 0
    mode = ""
    tests ={
        "тест 1":
        {
            1 : ("/home/konstantin/testBot/test1/1.png", "0","при делении двух целых чисел в языке Си, оператор \"/\"зж работает, как целочисленное деление. То есть деление с отбрасыванием остатка. Правильный ответ: 0"),
            2 : ("/home/konstantin/testBot/test1/2.png","UB","индексация массивов начинается с нуля.В данном случае, существуют элементы с индексами от 0 до 6 включительно. Элемента с индексом 7 не существует. Правильный ответ: UB"),
            3 : ("/home/konstantin/testBot/test1/3.png","hello\nworld","\\n является символом переноса строки. Все, что идет после этого символа будет выведено с новой строки. Правильный ответ: \"hello\nworld\""),
            4 : ("/home/konstantin/testBot/test1/4.png","helloworld","printf не ставит пробелы и переносы строк автоматически. Правильный ответ \"helloworld\""),
            5 : ("/home/konstantin/testBot/test1/5.png","12345678910","цикл будет выполнен 10 раз, пока переменная i будет меньше 10. На экран выводится i+1, поэтому значения напечатаются от 1 до 10. Правильный ответ: 12345678910")        
        }
    }
    rating = 0

    def result(self):
        result = f"правильно отвечено на : {self.goodAnswers} из {self.quantity} вопросов"

        rating = ceil(self.goodAnswers / self.quantity * 5)
        if rating < 2:
            rating = 2
        self.rating = int(rating)

        result += f"\nи получена оценка {int(rating)}.\n"
        string_array = ("Не расстраивайся",
                        "Не расстраивайся", "Ты можешь лучше",
                        "Неплохой результат",
                        "горжусь тобой")
        result += string_array[rating-1]
        return result
