from moviepy.editor import *
from config import VIDEOS, PATH, MEDIA
from utils.handler_title import convert_video_title


def converter_to_mp3(url_video: str, video_title: str):

    video = VideoFileClip(url_video)
    video_name = convert_video_title(video_title)
    video.audio.write_audiofile(os.path.join(PATH, MEDIA, video_title, VIDEOS, video_name))

    return video
