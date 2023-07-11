import os.path

from aiogram import Dispatcher
from aiogram.utils.exceptions import FileIsTooBig, NotFound
from aiogram.types import Message
from create_bot import bot
from config import VIDEOS, PATH, MEDIA
from utils.processor import converter_to_mp3
from utils.handler_title import convert_video_title
from moviepy.editor import *


async def convert_audio(msg: Message):
    chat_id = msg.chat.id
    video_id = msg.video.file_id

    try:
        await bot.send_message(chat_id, 'Loading ⏳')
        video_name = msg.video.file_name

        if not os.path.exists(os.path.join(PATH, MEDIA, video_name, VIDEOS)):
            video = await msg.video.download(destination_dir=os.path.join(PATH, MEDIA, video_name))

            video_dir = os.path.join(PATH, MEDIA, video_name, VIDEOS)

            save_video = []
            for file in os.listdir(video_dir):
                save_video.append(file)

            converter_to_mp3(str(os.path.join(video_dir, save_video[0])), video_name)
            audio_name = convert_video_title(video_name)

            audio_path = os.path.join(PATH, MEDIA, video_name, VIDEOS, audio_name)

            with open(audio_path, mode='rb') as file:
                audio = file.read()
                await bot.send_audio(chat_id=chat_id, audio=audio, title=audio_name.split('.')[0])
                file.close()
        else:
            for file in os.listdir(os.path.join(PATH, MEDIA, video_name, VIDEOS)):
                if file.endswith(".mp3"):
                    audio_title = file.split('.')[0]
                    with open(os.path.join(PATH, MEDIA, video_name, VIDEOS, file), mode='rb') as file:
                        audio = file.read()
                        await bot.send_audio(chat_id=chat_id, audio=audio, title=audio_title)
                        file.close()

    except FileIsTooBig as ex:
        print(ex)
        await msg.reply("You can't download more 20MB")


def register_handler_convert_audio(dp: Dispatcher):
    dp.register_message_handler(convert_audio, content_types=['video'])
