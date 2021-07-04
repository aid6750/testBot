from aiogram import Bot, Dispatcher, executor
from config import TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


if __name__ == "__main__":
    from handlers import dp
    executor.start_polling(dp)
