from aiogram import types
from aiogram.dispatcher import Dispatcher
from Bot.lexicon.lexicon import LEXICON_RU
from Bot.keyboard.keyboard import keyboard
from aiogram.types import CallbackQuery

# Регистрация хэндлеров
def register_keyboard_handlers(dp: Dispatcher):
    @dp.message_handler(commands=['start'])
    async def process_command_start(message: types.Message):
        await message.answer(
            text='Выберите категорию:',
            reply_markup=keyboard
        )

    @dp.callback_query_handler(lambda F: F.data == 'short_summary_button_pressed')
    async def process_short_summary_press(callback: CallbackQuery):
        await callback.message.edit_text(
            text=LEXICON_RU['short_summary'],
            reply_markup=callback.message.reply_markup
        )
        await callback.answer()

    @dp.callback_query_handler(lambda F: F.data == 'experience_button_pressed')
    async def process_experience_button_press(callback: CallbackQuery):
        await callback.message.edit_text(
            text=LEXICON_RU['experience'],
            reply_markup=callback.message.reply_markup
        )
        await callback.answer()

    @dp.callback_query_handler(lambda F: F.data == 'stak_button_pressed')
    async def process_stak_button_press(callback: CallbackQuery):
        await callback.message.edit_text(
            text=LEXICON_RU['stak'],
            reply_markup=callback.message.reply_markup
        )
        await callback.answer()

    @dp.callback_query_handler(lambda F: F.data == 'contacts_button_pressed')
    async def process_contacts_button_press(callback: CallbackQuery):
        await callback.message.edit_text(
            text=LEXICON_RU['contacts'],
            reply_markup=callback.message.reply_markup
        )
        await callback.answer()