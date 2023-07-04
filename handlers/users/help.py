from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher.filters import CommandHelp
from create_bot import bot


async def help(msg: Message):
    chat_id = msg.chat.id
    await bot.send_message(chat_id, 'Supported formats:\n\n'
                                    '🎧 Audio types: MP3')


def register_handler_help(dp: Dispatcher):
    dp.register_message_handler(help, CommandHelp(), state='*')


