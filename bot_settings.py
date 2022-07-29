from aiogram import Bot, Dispatcher
from decouple import config

bot = Bot(token=config('API_TOKEN'))
dp = Dispatcher(bot)
