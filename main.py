import asyncio
from aiogram import executor
from bot_settings import dp
from db_api.create_tables import create_users_table
from services import send_welcome, show_info, get_random, search_page


def register_handlers() -> None:
    dp.register_message_handler(send_welcome, commands=['start', 'info'])
    dp.register_message_handler(show_info, commands=['help'])
    dp.register_message_handler(get_random, commands=['get_random'])
    dp.register_message_handler(search_page, commands=['search'])


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(create_users_table())
    register_handlers()
    executor.start_polling(dp, skip_updates=True)
