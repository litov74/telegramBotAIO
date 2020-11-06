from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
choice2 = InlineKeyboardMarkup(row_width=1)

team = InlineKeyboardButton(text="⬇ ⬇ ⬇", callback_data="divide:0")
choice2.insert(team)