import logging
from aiogram.types import CallbackQuery
from links import clientsChatLink
from keyboards.inline.bestChoiceKb2 import choice2
from keyboards.inline.choosePhoto import photos as photoCat
from loader import dp
from keyboards.inline.divider import choice2 as division
from strings import textsForClients0, textsForClients1, textsForClients2, howToUseLeaflets, chooseInteresting, \
    currentLang
from keyboards.inline.clientsChat import clients
from keyboards.inline.fwdBwdForSecondText import choice as secondChoice
from keyboards.inline.fwdBwdForFirstText import choice as firstChoice
from keyboards.inline.fwdBwdForThirdText import choice as thirdChoice
from keyboards.inline.fwdBwdForFourthText import choice as fourthChoice
@dp.callback_query_handler(text_contains="client:video")
async def clientsVideo(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    await call.message.delete()
    await call.message.answer(clientsChatLink, reply_markup=clients)

@dp.callback_query_handler(text_contains="client:photo")
async def clientsPhoto(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    await call.message.answer(text="OK", reply_markup=photoCat)

@dp.callback_query_handler(text_contains="client:text")
async def clientsText(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    await call.message.answer(text=textsForClients0, reply_markup=firstChoice)

@dp.callback_query_handler(text_contains="toText:0")
async def toText0(call: CallbackQuery):
    global textNumber
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    await call.message.delete()
    await call.message.answer(text=textsForClients0, reply_markup=firstChoice)

@dp.callback_query_handler(text_contains="toText:1")
async def toText1(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    await call.message.delete()
    await call.message.answer(text=textsForClients1, reply_markup=secondChoice)

@dp.callback_query_handler(text_contains="toText:2")
async def toText2(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    await call.message.delete()
    await call.message.answer(text=textsForClients2, reply_markup=thirdChoice)

@dp.callback_query_handler(text_contains="toText:3")
async def toText3(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    await call.message.delete()
    await call.message.answer(text=howToUseLeaflets, reply_markup=fourthChoice)

@dp.callback_query_handler(text_contains="backToClientsMenu:0")
async def backToClientsMenu(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    await call.message.delete()

@dp.callback_query_handler(text_contains="divide:0")
async def divideText(call: CallbackQuery):
    await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains="nextpage:to2")
async def stepBack(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    await call.message.edit_reply_markup(reply_markup=choice2)

@dp.callback_query_handler(text_contains="clients:main")
async def backToMain(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    await call.message.edit_reply_markup(reply_markup=clients)

