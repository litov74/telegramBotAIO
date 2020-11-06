from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from strings import backKey, currentLang

texts = InlineKeyboardMarkup(row_width=2)

c1 = InlineKeyboardButton(text="⬅", callback_data="client:Textback")
texts.insert(c1)
c2 = InlineKeyboardButton(text="➡", callback_data="client:Textforward")
texts.insert(c2)
c3 = InlineKeyboardButton(text=backKey[currentLang], callback_data="clients:main")
texts.insert(c3)