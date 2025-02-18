from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

short_summary_button = InlineKeyboardButton(
    text='Короткое резюме',
    callback_data='short_summary_button_pressed'
)

experience_button = InlineKeyboardButton(
    text='Мой опыт',
    callback_data='experience_button_pressed'
)

stak_button = InlineKeyboardButton(
    text='Стек',
    callback_data='stak_button_pressed'
)

contacts_button = InlineKeyboardButton(
    text='Контакты',
    callback_data='contacts_button_pressed'
)

# Создание клавиатуры
keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[short_summary_button],
                     [experience_button],
                     [stak_button],
                     [contacts_button]]
)
