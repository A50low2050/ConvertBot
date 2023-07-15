from aiogram import Dispatcher
from aiogram.types import CallbackQuery
from keyboards.admin_keyboards import admin_panels


async def admin_panel(call: CallbackQuery):
    await call.message.edit_text('Welcome in admin panel', reply_markup=admin_panels())


def register_handler_admin_panel(dp: Dispatcher):
    dp.register_callback_query_handler(admin_panel, text='admin_panel')
