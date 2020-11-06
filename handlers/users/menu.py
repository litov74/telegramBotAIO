from aiogram.dispatcher.filters import Command, Text
from loader import dp
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import main
from strings import bestChoiceBtn, contractActivationBtn, howToStartBtn, chooseLanguageBtn, currentLang, whileLoading, \
    chooseInteresting, settingsBtn, becomeProSlogan, schoolHash, ludiMiraHash

from links import howToActivateFirstContractLink, firstStepsInBusinessLink
from keyboards.inline.bestChoiceKb import choice
from keyboards.default.backDefault import backKeyboard

@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer("Ok", reply_markup=main)


@dp.message_handler(Text(equals=[bestChoiceBtn[currentLang]]))
async def best_choice(message: Message):
    await message.answer(f"{message.text}", reply_markup=choice)
    #await message.answer("Отлично!;)", reply_markup=choice)

@dp.message_handler(Text(equals=[contractActivationBtn[currentLang]]))
async def contract_activation(message: Message):
    await message.answer(f"{message.text}", reply_markup=ReplyKeyboardRemove())
    await message.answer(howToActivateFirstContractLink +"\n\n"+ schoolHash, reply_markup=main)

@dp.message_handler(Text(equals=[howToStartBtn[currentLang]]))
async def starters(message: Message):
    await message.answer(f"{message.text}", reply_markup=ReplyKeyboardRemove())
    await message.answer(firstStepsInBusinessLink +"\n\n"+ ludiMiraHash, reply_markup=main)

@dp.message_handler(Text(equals=["Вернуться"]))
async def backInBlack(message: Message):
    await message.answer(f"{message.text}", reply_markup=main)
