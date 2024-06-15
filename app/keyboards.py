from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text = "Каталог")],
    [KeyboardButton(text = "Корзина"), KeyboardButton(text = "Контакты")]
],resize_keyboards = True,
input_field_placeholder = "Выберите пункт меню.")