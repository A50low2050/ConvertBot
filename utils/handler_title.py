

def convert_video_title(video_title: str):
    convert_title = video_title.split('.')[0]
    type_file = '.mp3'
    title_to_mp3 = convert_title + type_file
    return title_to_mp3
