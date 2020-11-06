from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from strings import bestChoiceBtn, contractActivationBtn, howToStartBtn, settingsBtn, currentLang
backKeyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Вернуться")
        ],

], resize_keyboard=True)