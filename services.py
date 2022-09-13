import wikipedia
from aiogram import types
from bot_settings import dp
from db_api.db_commands import add_user
from utils import user_is_allowed
from logger import logger_info


@dp.message_handler(commands=['start', 'info'])
async def send_welcome(message: types.Message):
    """ This handler will be called when user sends `/start` or `/help` command """
    logger_info(send_welcome)
    await add_user(message)

    await message.reply("Hi!\n"
                        "I'm Random Wiki Learner Bot!\n"
                        "I can help you to expand your horizons by giving you random articles everyday.\n"
                        "To learn about commands please press /help")


@dp.message_handler(commands=['help'])
async def show_info(message: types.Message):
    """ This handler will show bot information. """
    logger_info(show_info)

    await message.reply("Commands:\n"
                        "   * /start - to start chat with bot.\n"
                        "   * /help - commands information.\n"
                        "   * /get_random - get random wiki page.\n"
                        "   * /search - enables to search article in wikipedia.")


@dp.message_handler(commands=['get_random'])
async def get_random(message: types.Message):
    """ This handler will show random article from wikipedia. """
    logger_info(get_random)

    if not user_is_allowed(message):
        return await message.reply("Sorry, you do not have permission to use this bot.")

    try:
        random_wiki_page = wikipedia.random(1)
        result = wikipedia.page(random_wiki_page)
        await message.reply(f"Today's article is dedicated to {result.title}.\n"
                            f"To learn more: {result.url}", reply=False)

    except wikipedia.DisambiguationError:
        await message.reply("We have too much results...", reply=False)


@dp.message_handler(commands=['search'])
async def search_page(message: types.Message):
    """ This handler enables to search article in wikipedia. """
    logger_info(search_page)

    if not user_is_allowed(message):
        return await message.reply("Sorry, you do not have permission to use this bot.")

    await message.reply("Sorry, this command is under development...", reply=False)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)
