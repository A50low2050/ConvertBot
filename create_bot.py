from aiogram import Bot, Dispatcher
from config import TOKEN


bot = Bot(token=TOKEN, parse_mode='HTML', disable_web_page_preview=True)
dp = Dispatcher(bot)
