import logging
from aiogram.types import Message, CallbackQuery
from strings import chooseInteresting, currentLang, meetingDisclaimerText, disagreementHowToReply, disagreementStep1Text, disagreementStep2Text, disagreementStep3Text, disagreementStep4Text, disagreementStep5Text
from loader import dp
from keyboards.inline.disagreementKb import dis

@dp.callback_query_handler(text_contains="beginning:0")
async def dis_beginning(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer(meetingDisclaimerText +"\n\n"+ disagreementHowToReply, reply_markup=dis)


@dp.callback_query_handler(text_contains="step:1")
async def stepOne(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer(disagreementStep1Text, reply_markup=dis)


@dp.callback_query_handler(text_contains="step:2")
async def stepTwo(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer(disagreementStep2Text, reply_markup=dis)


@dp.callback_query_handler(text_contains="step:3")
async def stepThree(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer(disagreementStep3Text, reply_markup=dis)


@dp.callback_query_handler(text_contains="step:4")
async def stepFour(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer(disagreementStep4Text, reply_markup=dis)


@dp.callback_query_handler(text_contains="step:5")
async def stepFive(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer(disagreementStep5Text, reply_markup=dis)

@dp.callback_query_handler(text_contains="step:6")
async def stepSix(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_audio(audio=open("audios/disagreement1.ogg","rb"), reply_markup=None)
    await call.message.answer_audio(audio=open("audios/disagreement2.ogg","rb"), reply_markup=dis)

