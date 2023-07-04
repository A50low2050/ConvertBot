from aiogram import Dispatcher
from aiogram.utils.exceptions import FileIsTooBig
from aiogram.types import Message
from create_bot import bot
from config import TOKEN, PATH, MEDIA
from utils.processor import converter_to_mp3
from utils.handler_title import convert_video_title
from moviepy.editor import *


async def convert_audio(msg: Message):
    chat_id = msg.chat.id
    video_id = msg.video.file_id

    try:
        await bot.send_message(chat_id, 'Loading ⏳')
        file = await bot.get_file(video_id)
        download_url = f"https://api.telegram.org/file/bot{TOKEN}/{file.file_path}"
        video_name = msg.video.file_name

        converter_to_mp3(download_url, video_name)
        audio_name = convert_video_title(video_name)

        audio_path = os.path.join(PATH, MEDIA, audio_name)

        with open(audio_path, mode='rb') as file:
            audio = file.read()
            await bot.send_audio(chat_id=chat_id, audio=audio, title=audio_name.split('.')[0])

    except FileIsTooBig as ex:
        print(ex)
        await msg.reply("You can't download more 20MB")


def register_handler_convert_audio(dp: Dispatcher):
    dp.register_message_handler(convert_audio, content_types=['video'])
