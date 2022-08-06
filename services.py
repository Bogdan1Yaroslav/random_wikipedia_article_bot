import logging
import wikipedia
from aiogram import types
from datetime import datetime

from bot_settings import bot, dp
from utils import user_is_allowed

logging.basicConfig(level=logging.INFO)

# requested_at = datetime.now().strftime("%d.%m.%Y %H:%M:%S")


@dp.message_handler(commands=['start', 'info'])
async def send_welcome(message: types.Message):
    """ This handler will be called when user sends `/start` or `/help` command """

    await message.reply("Hi!\n"
                        "I'm Random Wiki Learner Bot!\n"
                        "I can help you to expand your horizons by giving you random articles everyday.\n"
                        "To learn about commands please press /help")


@dp.message_handler(commands=['help'])
async def show_info(message: types.Message):
    """ This handler will show bot information. """

    await message.reply("Commands:\n"
                        "   * /start - to start chat with bot.\n"
                        "   * /help - commands information.\n"
                        "   * /get_random - get random wiki page.\n"
                        "   * /search - enables to search article in wikipedia.")


@dp.message_handler(commands=['get_random'])
async def get_random(message: types.Message):
    """ This handler will show random article from wikipedia. """

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

    if not user_is_allowed(message):
        return await message.reply("Sorry, you do not have permission to use this bot.")

    msg = await bot.send_message(message.from_user.id, "Enter your search topic")

    print(msg.text)

    # try:
    #
    # except wikipedia.exceptions.DisambiguationError as e:
    #     await message.reply("Page not found.")

    # random_wiki_page = wikipedia.random(1)
    #
    # result = wikipedia.page(random_wiki_page)
    # # print(result.summary)
    # await message.reply(f"Today's article is dedicated to {result.title}.\n"
    #                     f"To learn more: {result.url}", reply=False)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)
