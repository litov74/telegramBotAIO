from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from strings import greetingText, currentLang, helloText
from loader import dp

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    s = str(helloText[currentLang] + message.from_user.full_name + "!\n\n"+ greetingText[currentLang])
    await message.answer(s)
