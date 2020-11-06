from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from strings import teamSystemBtn,first10Days, cartReviewBtn, businessAdBtn, makeACallBtn, disagreementBtn, currentLang, understandBusinessBtn


choice = InlineKeyboardMarkup(row_width=1)
team = InlineKeyboardButton(text=teamSystemBtn[currentLang], callback_data="teamSystem:0")
team1 = InlineKeyboardButton(text=cartReviewBtn[currentLang], callback_data="cartReview:0")
team2 = InlineKeyboardButton(text=businessAdBtn[currentLang], callback_data="businessAd:0")
team3 = InlineKeyboardButton(text=understandBusinessBtn[currentLang], callback_data="getout:0")
team4 = InlineKeyboardButton(text=disagreementBtn[currentLang], callback_data="disagreement:0")
team5 = InlineKeyboardButton(text=first10Days[currentLang], callback_data="first:days")
next_page = InlineKeyboardButton(text="Следующая страница", callback_data="nextpage:0")


choice.insert(team)
choice.insert(team1)
choice.insert(team2)
choice.insert(team3)
choice.insert(team4)
choice.insert(team5)
choice.insert(next_page)

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
