from aiogram import executor
from create_bot import dp


async def on_startup(dp):
    print('Bot launch')

    from handlers.users import start, video
    start.register_handler_start(dp)
    video.register_handler_convert_audio(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
