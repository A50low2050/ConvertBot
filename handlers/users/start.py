from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher.filters import CommandStart
from create_bot import bot


async def start(msg: Message):
    chat_id = msg.chat.id
    first_name = msg.from_user.first_name
    await bot.send_message(chat_id, f'Привет {first_name}')


def register_handler_start(dp: Dispatcher):
    dp.register_message_handler(start, CommandStart(), state='*')


