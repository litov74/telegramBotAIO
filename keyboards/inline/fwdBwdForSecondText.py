from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

choice = InlineKeyboardMarkup(row_width=1)

c1 = InlineKeyboardButton(text="К следующему примеру ➡", callback_data="toText:2")
c2 = InlineKeyboardButton(text="⬅ К предыдущему примеру", callback_data="toText:0")
choice.insert(c1)
choice.insert(c2)
c3 = InlineKeyboardButton(text="К меню клиентского чата", callback_data="backToClientsMenu:0")
choice.insert(c3)
