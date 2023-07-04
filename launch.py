from aiogram import executor
from create_bot import dp
from create_bot import bot
from utils.commands import set_commands


async def on_startup(dp):
    print('Bot launch')
    await set_commands(bot)

    from handlers.users import start, help, video

    start.register_handler_start(dp)
    help.register_handler_help(dp)

    video.register_handler_convert_audio(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
