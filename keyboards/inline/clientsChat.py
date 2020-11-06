from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from strings import videoBtn, currentLang, photoBtn, textBtn, backKey

clients = InlineKeyboardMarkup(row_width=1)

c1 = InlineKeyboardButton(text=videoBtn[currentLang], callback_data="client:video")
clients.insert(c1)
c2 = InlineKeyboardButton(text=photoBtn[currentLang], callback_data="client:photo")
clients.insert(c2)
c3 = InlineKeyboardButton(text=textBtn[currentLang], callback_data="client:text")
clients.insert(c3)
c4 = InlineKeyboardButton(text=backKey[currentLang], callback_data="nextpage:to2")
clients.insert(c4)