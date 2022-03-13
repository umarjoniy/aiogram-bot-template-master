from . import commands,no_state,with_state
from aiogram import types, Dispatcher
#from aiogram.dispatcher.filters.builtin import CommandStart,CommandHelp
from loader import dp

def register_user_handler(dp:Dispatcher):
    dp.register_message_handler(commands.commands, commands=['start', 'help'])
    dp.register_message_handler(no_state.no_state, state=None)
    dp.register_message_handler(with_state.with_state, state='*')