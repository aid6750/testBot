import asyncio
from aiogram import Bot, Dispatcher, executor
from config import TOKEN
loop = asyncio.get_event_loop()
bot = Bot(TOKEN)
dp = Dispatcher(bot, loop=loop)


if __name__ == "__main__":
    from handlers import dp
    executor.start_polling(dp)
