import logging
from aiogram.types import CallbackQuery
from strings import *
from keyboards.inline.bestChoiceKb2 import choice2
from keyboards.inline.bestChoiceKb3 import choice3
from loader import dp
from links import *
from keyboards.inline.langKeyboard import lang

@dp.callback_query_handler(text_contains="makeOrder:0")
async def team_system(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer(howToMakeAnOrderLink +"\n\n"+ becomeProSlogan[currentLang], reply_markup=choice3)

@dp.callback_query_handler(text_contains="registerPartner:0")
async def cartReview(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer(howToRegisterPartnerLink +"\n\n"+ getInSchoolSlogan[currentLang], reply_markup=choice3)

@dp.callback_query_handler(text_contains='contractSets:0')
async def business(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer(contractActivationSetsLink +"\n\n"+ joinTeamSlogan[currentLang], reply_markup=choice3)

@dp.callback_query_handler(text_contains='trackOrder:0') ##UNDONE
async def makeACall(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer(howToTrackAnOrderLink +"\n\n"+ becomeProSlogan[currentLang], reply_markup=choice3)

@dp.callback_query_handler(text_contains='purchReport:0')
async def purchReport(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer(howToGetAPurchaseReportLink +"\n\n"+ getInSchoolSlogan[currentLang], reply_markup=choice3)

@dp.callback_query_handler(text_contains='lingua:0')
async def lingua(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_document(document=open("books/100_вопросов.pdf", "rb"), reply_markup=choice3)

@dp.callback_query_handler(text_contains='backward:2')
async def lingua(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.edit_reply_markup(reply_markup=choice2)

