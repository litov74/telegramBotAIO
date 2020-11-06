from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from strings import *
from strings import langKeys

lang = InlineKeyboardMarkup(row_width=1)

rus = InlineKeyboardButton(text=langKeys[0], callback_data="langRU:0")
lang.insert(rus)
eng = InlineKeyboardButton(text=langKeys[1], callback_data="langEN:0")
lang.insert(eng)
de = InlineKeyboardButton(text=langKeys[2], callback_data="langDE:0")
lang.insert(de)
cancel_button = InlineKeyboardButton(text="Отмена", callback_data="cancelLING:0")
lang.insert(cancel_button)