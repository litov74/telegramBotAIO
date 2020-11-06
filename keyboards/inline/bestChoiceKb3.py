from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from strings import *
from keyboards.inline.callBackPath import pathCall

choice3 = InlineKeyboardMarkup(row_width=1)

team = InlineKeyboardButton(text=howToMakeAnOrderBtn[currentLang], callback_data="makeOrder:0")
choice3.insert(team)
team1 = InlineKeyboardButton(text=registerPeopleBtn[currentLang], callback_data="registerPartner:0")
choice3.insert(team1)
team2 = InlineKeyboardButton(text=topTenBtn[currentLang], callback_data="contractSets:0")
choice3.insert(team2)
team3 = InlineKeyboardButton(text=howToTrackAnOrderBtn[currentLang], callback_data="trackOrder:0")
choice3.insert(team3)
team4 = InlineKeyboardButton(text=howToGetAPurchaseReportBtn[currentLang], callback_data="purchReport:0")
choice3.insert(team4)
team5 = InlineKeyboardButton(text=top100Questions[currentLang], callback_data="lingua:0")
choice3.insert(team5)
next_page = InlineKeyboardButton(text="Предыдущая страница", callback_data="backward:2")
choice3.insert(next_page)


# А теперь клавиатуры со ссылками на товары
#pear_keyboard = InlineKeyboardMarkup(inline_keyboard=[
#    [
#        InlineKeyboardButton(text="Купи тут", url="x")
#    ]
#])
#apples_keyboard = InlineKeyboardMarkup(inline_keyboard=[
#    [
#        InlineKeyboardButton(text="Купи тут", url="x")
#    ]
#])
