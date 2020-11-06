from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from strings import bestChoiceBtn, contractActivationBtn, howToStartBtn, settingsBtn, currentLang
mainKeyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=bestChoiceBtn[currentLang]), KeyboardButton(text=contractActivationBtn[currentLang])
        ],
        [
            KeyboardButton(text=howToStartBtn[currentLang])
        ],

], resize_keyboard=True)