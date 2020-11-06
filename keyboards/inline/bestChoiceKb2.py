from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from strings import *
from keyboards.inline.callBackPath import pathCall

choice2 = InlineKeyboardMarkup(row_width=1)

team = InlineKeyboardButton(text=marketingBtn[currentLang], callback_data="marketing:0")
choice2.insert(team)
team1 = InlineKeyboardButton(text=clientsChatBtn[currentLang], callback_data="clientsChat:0")
choice2.insert(team1)
team2 = InlineKeyboardButton(text=makeATopTenBtn[currentLang], callback_data="makeATopTen:0")
choice2.insert(team2)
#team3 = InlineKeyboardButton(text=meetingSampleBtn[currentLang], callback_data="meetingSample:0")
#choice2.insert(team3)
team4 = InlineKeyboardButton(text=howToContactUsBtn[currentLang], callback_data="contactUS:0")
choice2.insert(team4)
team5 = InlineKeyboardButton(text=howToMakeACall[currentLang], callback_data="business:call")
choice2.insert(team5)
back_page = InlineKeyboardButton(text="Предыдущая страница", callback_data="backward:0")
choice2.insert(back_page)
next_page = InlineKeyboardButton(text="Следующая страница", callback_data="nextpage:1")
choice2.insert(next_page)
