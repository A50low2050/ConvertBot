from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher.filters import CommandStart
from create_bot import bot
from config import ADMIN
from keyboards.admin_keyboards import admin_menu


async def start(msg: Message):
    chat_id = msg.chat.id
    first_name = msg.from_user.first_name

    if chat_id == int(ADMIN):
        await bot.send_message(chat_id, f'Hi {first_name}🖐\n'
                                        f'To convert a video to MP3 format, download a video with MP4 resolution.\n\n'
                                        f'📌 Bot can download files of up to 20MB in size <a href="https://core.telegram.org/bots/api#getfile">limit Telegram</a>.',
                               reply_markup=admin_menu())
    else:
        await bot.send_message(chat_id, f'Hi {first_name}🖐\n'
                                        f'To convert a video to MP3 format, download a video with MP4 resolution.\n\n'
                                        f'📌 Bot can download files of up to 20MB in size <a href="https://core.telegram.org/bots/api#getfile">limit Telegram</a>.')


def register_handler_start(dp: Dispatcher):
    dp.register_message_handler(start, CommandStart(), state='*')


