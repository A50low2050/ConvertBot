import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN_BOT')
ADMIN = os.getenv('ADMIN')

PATH = os.path.dirname(os.path.abspath(__file__))
MEDIA = 'media'
VIDEOS = 'videos'
