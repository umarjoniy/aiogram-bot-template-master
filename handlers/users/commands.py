from aiogram import types

from loader import bot


async def commands(message: types.Message):
    if message.text == "/start":
        await main(message)

async def main( message: types.Message):
    await bot.send_message(message.from_user.id,'<code>/start</code>')