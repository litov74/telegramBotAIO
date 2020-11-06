from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from strings import backKey, currentLang

photos = InlineKeyboardMarkup(row_width=2)

c1 = InlineKeyboardButton(text="⬅", callback_data="client:back")
photos.insert(c1)
c2 = InlineKeyboardButton(text="➡", callback_data="client:forward")
photos.insert(c2)
c3 = InlineKeyboardButton(text=backKey[currentLang], callback_data="clients:main")
photos.insert(c3)