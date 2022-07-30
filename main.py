import logging
from aiogram import executor, types
from bot_settings import dp
from utils import user_is_allowed

logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """ This handler will be called when user sends `/start` or `/help` command """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler(commands=['info'])
async def show_info(message: types.Message):
    """ This handler will show bot information. """

    if not user_is_allowed(message):
        return await message.reply("Sorry, you do not have permission to use this bot.")

    await message.reply("Hi!\n"
                        "I'm Random Wiki Learner Bot!\n"
                        "I can help you to expand your horizons by giving you random articles everyday.")


@dp.message_handler(commands=['get_random'])
async def get_random(message: types.Message):
    """ This handler will show random article from wikipedia. """

    if not user_is_allowed(message):
        return await message.reply("Sorry, you do not have permission to use this bot.")

    await message.reply("The command is under development...")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
