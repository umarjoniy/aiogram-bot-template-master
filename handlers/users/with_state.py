from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import bot

async def with_state(self,message:types.Message,state: FSMContext):
    if await state.get_state() == "main":
        await self.main(message,state)

async def main(message:types.Message,state: FSMContext):
    await bot.send_message(message.from_user.id,f"Привет! \n<code>{await state.get_state()}</code>")
