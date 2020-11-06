import logging

from aiogram.types import CallbackQuery
from keyboards.inline.bestChoiceKb3 import choice3
from loader import dp, bot
from strings import langKeys



@dp.callback_query_handler(text_contains="langRU:0")
async def set_RUS(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    from strings import currentLang
    if currentLang != 0:
        currentLang = 0
        await bot.get_updates()
    await call.message.answer(langKeys[currentLang], reply_markup=choice3)

@dp.callback_query_handler(text_contains="langEN:0")
async def set_ENG(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")

    from strings import currentLang
    if currentLang != 1:
        currentLang = 1
        await bot.get_updates()
    await call.message.answer(langKeys[currentLang], reply_markup=choice3)

@dp.callback_query_handler(text_contains="langDE:0")
async def set_DEU(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    from strings import currentLang
    if currentLang != 2:
        currentLang = 2
        await bot.get_updates()
    await call.message.answer(langKeys[currentLang], reply_markup=choice3)
@dp.callback_query_handler(text_contains="cancelLING:0")
async def get_back_mfck(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    from strings import currentLang
    await bot.get_updates()
    await call.message.answer(langKeys[currentLang], reply_markup=choice3)

