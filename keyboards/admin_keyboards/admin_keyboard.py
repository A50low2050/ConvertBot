from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def admin_menu():

    admin_menu = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Admin Panel', callback_data='admin_panel'),
            ],
        ]
    )

    return admin_menu


def admin_panels():

    admin_panels = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='🧹Clear Media', callback_data='clear_media'),
                InlineKeyboardButton(text='👁️Show Media', callback_data='show_media'),
            ],

        ]
    )

    return admin_panels
