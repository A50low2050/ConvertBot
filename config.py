import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN_BOT')

PATH = os.path.dirname(os.path.abspath(__file__))
MEDIA = 'media'
