"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging


import wikipedia
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5149918830:AAED3NUaHEAtg38L-deeNWd-kXTncppD1qg'
wikipedia.set_lang('uz')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Wikipediya botiga xush kelibsiz.")



@dp.message_handler()
async def sendWiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer('Bu mavzuga oid mavzu topilmadi')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)