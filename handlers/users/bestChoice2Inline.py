import logging
from aiogram.types import CallbackQuery
from keyboards.inline.bestChoiceKb3 import choice3
from strings import *
from keyboards.inline.bestChoiceKb import choice
from keyboards.inline.bestChoiceKb2 import choice2
from keyboards.inline.clientsChat import clients
from loader import dp
from links import *

@dp.callback_query_handler(text_contains='marketing:0')
async def marketing(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer(text=marketingLink +"\n\n"+ becomeProSlogan[currentLang], reply_markup=choice2)

@dp.callback_query_handler(text_contains='clientsChat:0')
async def clientsChat(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer(clientsChatBtn[currentLang], reply_markup=clients)

@dp.callback_query_handler(text_contains='makeATopTen:0')
async def makeATopTen(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer("Вы можете изучить подробнее в книге..." +"\n\n"+ getInSchoolSlogan[currentLang], reply_markup=None)
    await call.message.answer_document(document=open("books/10_аргументов.pdf", "rb"), reply_markup=choice2)

@dp.callback_query_handler(text_contains='meetingSample:0')
async def meetingSample(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer(text="Скоро тут будет расписана структура встречи", reply_markup=choice2)

@dp.callback_query_handler(text_contains='contactUS:0')
async def contactUS(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer(text=howToContactUsLink +"\n\n"+ joinTeamSlogan[currentLang], reply_markup=choice2)

@dp.callback_query_handler(text_contains="business:call")
async def businessCall(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer(text=howToMakeCallLink +"\n\n"+ becomeProSlogan[currentLang], reply_markup=choice2)

@dp.callback_query_handler(text_contains="backward:0")
async def bwd(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.edit_reply_markup(reply_markup=choice)

@dp.callback_query_handler(text_contains="nextpage:1")
async def fwd(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.edit_reply_markup(reply_markup=choice3)