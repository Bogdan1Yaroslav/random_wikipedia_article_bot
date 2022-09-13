import logging
from asyncpg import UniqueViolationError, connect
from aiogram import types
from bot_settings import db_URI


async def add_user(message: types.Message):
    conn = await connect(db_URI)
    user_id, name = message.from_user.id, message.from_user.first_name
    try:
        # print(f"Connecting to DB")
        logging.info("Connecting to DB")

        async with conn.transaction():
            await conn.execute('''
                INSERT INTO users(id, name) VALUES($1, $2)
            ''', user_id, name)

        # print(f"User named {name} with id {user_id} was created!")
        logging.info(f"User named {name} with id {user_id} was created!")

    except UniqueViolationError:
        # print(f"User named {name} with id {user_id} was not created.")
        logging.info(f"User named {name} with id {user_id} was not created.")
    finally:
        await conn.close()
