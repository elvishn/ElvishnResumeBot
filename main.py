import asyncio
from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers.handlers import register_keyboard_handlers

async def main():
    config = load_config()
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher(bot=bot)
    register_keyboard_handlers(dp)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling()

asyncio.run(main())
