from aiogram import types
from bot_settings import your_id


def user_is_allowed(message: types.Message) -> bool:
    user_id = message.from_user.id
    return True if user_id == your_id else False
