import asyncpg
from bot_settings import db_URI
import logging


async def create_users_table():
    # print(f"Connecting to DB")
    logging.info("Connecting to DB")

    conn = await asyncpg.connect(db_URI)
    async with conn.transaction():
        await conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
            id INT NOT NULL,
            Name VARCHAR(255) NOT NULL,
            PRIMARY KEY (id))
        ''')

    await conn.close()
    logging.info("Table has been created!")
    # print(f"Table has been created!")
