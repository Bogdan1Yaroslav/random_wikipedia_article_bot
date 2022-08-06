from aiogram import executor
from bot_settings import dp
from services import send_welcome, show_info, get_random, search_page


def register_handlers() -> None:
    dp.register_message_handler(send_welcome, commands=['start', 'info'])
    dp.register_message_handler(show_info, commands=['help'])
    dp.register_message_handler(get_random, commands=['get_random'])
    dp.register_message_handler(search_page, commands=['search'])


if __name__ == '__main__':
    register_handlers()
    executor.start_polling(dp, skip_updates=True)
