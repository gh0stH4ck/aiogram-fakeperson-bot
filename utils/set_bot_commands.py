from aiogram import types


async def set_default_commands(dp) -> None:
    """Установка команд для бота"""
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота"),
        types.BotCommand("help", "Помощь"),
    ])
