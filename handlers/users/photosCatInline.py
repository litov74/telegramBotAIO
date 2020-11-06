import logging
from aiogram.types import CallbackQuery
from keyboards.inline.choosePhoto import photos as photoCat
from loader import dp
from keyboards.inline.divider import choice2 as division
from keyboards.inline.clientsChat import clients

@dp.callback_query_handler(text_contains="cat:beauty")
async def catBeauty(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    await call.message.answer_photo(photo=open("photos/beauty/1.jpg", "rb"), reply_markup=division)
    await call.message.answer_photo(photo=open("photos/beauty/2.jpg", "rb"), reply_markup=division)
    await call.message.answer_photo(photo=open("photos/beauty/3.jpg", "rb"), reply_markup=photoCat)

@dp.callback_query_handler(text_contains="cat:food")
async def catFood(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    await call.message.answer_photo(photo=open("photos/foods/1.jpg", "rb"), reply_markup=photoCat)

@dp.callback_query_handler(text_contains="cat:health")
async def catHealth(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    await call.message.answer_photo(photo=open("photos/health/1.jpg", "rb"), reply_markup=photoCat)

@dp.callback_query_handler(text_contains="cat:house")
async def catHouse(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    await call.message.answer_photo(photo=open("photos/housekeeping/1.jpg", "rb"), reply_markup=division)
    await call.message.answer_photo(photo=open("photos/housekeeping/2.jpg", "rb"), reply_markup=division)
    await call.message.answer_photo(photo=open("photos/housekeeping/3.jpg", "rb"), reply_markup=division)
    await call.message.answer_photo(photo=open("photos/housekeeping/4.jpg", "rb"), reply_markup=photoCat)

@dp.callback_query_handler(text_contains="cat:shampoo")
async def catShampoo(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    await call.message.answer_photo(photo=open("photos/shampoos/1.jpg", "rb"), reply_markup=division)
    await call.message.answer_photo(photo=open("photos/shampoos/2.jpg", "rb"), reply_markup=division)
    await call.message.answer_photo(photo=open("photos/shampoos/3.jpg", "rb"), reply_markup=division)
    await call.message.answer_photo(photo=open("photos/shampoos/4.jpg", "rb"), reply_markup=division)
    await call.message.answer_photo(photo=open("photos/shampoos/5.jpg", "rb"), reply_markup=division)
    await call.message.answer_photo(photo=open("photos/shampoos/6.jpg", "rb"), reply_markup=division)
    await call.message.answer_photo(photo=open("photos/shampoos/7.jpg", "rb"), reply_markup=division)
    await call.message.answer_photo(photo=open("photos/shampoos/8.jpg", "rb"), reply_markup=photoCat)

@dp.callback_query_handler(text_contains="cat:soaps")
async def catSoap(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    await call.message.answer_photo(photo=open("photos/soaps/1.jpg", "rb"), reply_markup=division)
    await call.message.answer_photo(photo=open("photos/soaps/2.jpg", "rb"), reply_markup=division)
    await call.message.answer_photo(photo=open("photos/soaps/3.jpg", "rb"), reply_markup=division)
    await call.message.answer_photo(photo=open("photos/soaps/4.jpg", "rb"), reply_markup=photoCat)

@dp.callback_query_handler(text_contains="cat:teas")
async def catTea(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"callback_data='{callback_data}'")
    await call.message.answer_photo(photo=open("photos/teas/1.jpg", "rb"), reply_markup=division)
    await call.message.answer_photo(photo=open("photos/teas/2.jpg", "rb"), reply_markup=division)
    await call.message.answer_photo(photo=open("photos/teas/3.jpg", "rb"), reply_markup=division)
    await call.message.answer_photo(photo=open("photos/teas/4.jpg", "rb"), reply_markup=division)
    await call.message.answer_photo(photo=open("photos/teas/5.jpg", "rb"), reply_markup=division)
    await call.message.answer_photo(photo=open("photos/teas/6.jpg", "rb"), reply_markup=division)
    await call.message.answer_photo(photo=open("photos/teas/7.jpg", "rb"), reply_markup=division)
    await call.message.answer_photo(photo=open("photos/teas/8.jpg", "rb"), reply_markup=division)
    await call.message.answer_photo(photo=open("photos/teas/9.jpg", "rb"), reply_markup=division)
    await call.message.answer_photo(photo=open("photos/teas/10.jpg", "rb"), reply_markup=division)
    await call.message.answer_photo(photo=open("photos/teas/11.jpg", "rb"), reply_markup=division)
    await call.message.answer_photo(photo=open("photos/teas/12.jpg", "rb"), reply_markup=division)
    await call.message.answer_photo(photo=open("photos/teas/13.jpg", "rb"), reply_markup=division)
    await call.message.answer_photo(photo=open("photos/teas/14.jpg", "rb"), reply_markup=division)
    await call.message.answer_photo(photo=open("photos/teas/15.jpg", "rb"), reply_markup=photoCat)