from aiogram import Bot, Dispatcher
from decouple import config

bot = Bot(token=config('API_TOKEN'))
your_id = int(config('YOUR_ID'))
dp = Dispatcher(bot)

ip = config('ip')
db_user = config('PGUSER')
db_password = config('PGPASSWORD')
db_name = config('DATABASE')
db_URI = f"postgresql://{db_user}:{db_password}@{ip}/{db_name}"
