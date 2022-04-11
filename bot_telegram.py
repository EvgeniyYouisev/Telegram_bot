from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

@dp.message_handler()
async def forvard_send(massage : types.message):
    await massage.answer(massage.text)
    
executor.start_polling(dp, skip_updates=True)