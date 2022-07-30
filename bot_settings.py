from aiogram import Bot, Dispatcher
from decouple import config

bot = Bot(token=config('API_TOKEN'))
your_id = int(config('YOUR_ID'))
dp = Dispatcher(bot)
