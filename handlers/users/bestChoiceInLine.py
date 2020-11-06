import logging
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery
from strings import chooseInteresting, currentLang, becomeProSlogan, getInSchoolSlogan, joinTeamSlogan, ludiMiraHash, schoolHash
from keyboards.inline.bestChoiceKb import choice
from keyboards.inline.bestChoiceKb2 import choice2
from keyboards.inline.divider import choice2 as division
from loader import dp
from links import *
from strings import disagreementDisclaimerText, disagreementDisclaimer2Text
from keyboards.inline.disagreementKb import dis


@dp.message_handler(Command("items"))
async def show_items(message: Message):
    await message.answer(text=chooseInteresting[currentLang], reply_markup=choice)

@dp.callback_query_handler(text_contains="teamSystem:0")
async def team_system(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer(text=(teamSystemLink +"\n\n"+ becomeProSlogan[currentLang]), reply_markup=choice)

@dp.callback_query_handler(text_contains="cartReview:0")
async def cart_review(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer(cartReviewLink +"\n\n"+ getInSchoolSlogan[currentLang], reply_markup=choice)

@dp.callback_query_handler(text_contains='businessAd:0')
async def business(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer(howToMakeABusinessAdLink +"\n\n"+ joinTeamSlogan[currentLang], reply_markup=choice)

@dp.callback_query_handler(text_contains='disagreement:0') ##UNDONE
async def disagree(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer(text=disagreementDisclaimerText, reply_markup=division)
    await call.message.answer(text=disagreementDisclaimer2Text, reply_markup=dis)

@dp.callback_query_handler(text_contains="first:days")
async def firstDays(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_document(document=open("books/10_дней.pdf", "rb"), reply_markup=choice)


@dp.callback_query_handler(text_contains='getout:0') ##UNDONE
async def getOut(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_document(document=open("books/разберись_в_бизнесе.pdf", "rb"), reply_markup=choice)

@dp.callback_query_handler(text_contains="nextpage:0")
async def fwd(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.edit_reply_markup(reply_markup=choice2)