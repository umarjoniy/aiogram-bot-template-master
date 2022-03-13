from aiogram import types

from loader import bot


async def no_state(message: types.Message):
    if message.text == "main":
        await main(message)

async def main(message: types.Message):
    await bot.send_message(message.from_user.id, f"Привет! \n<code>{message}</code>")
