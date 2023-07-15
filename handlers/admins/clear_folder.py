from aiogram import Dispatcher
from utils.clear_media import clear_media
from aiogram.types import CallbackQuery
from create_bot import bot


async def clear_folder(call: CallbackQuery):
    msg_answer = clear_media()
    bot.answer_callback_query(call.id)
    await call.message.reply(msg_answer)


def register_handler_clear_folder(dp: Dispatcher):
    dp.register_callback_query_handler(clear_folder, text='clear_media')
