from aiogram import types
from aiogram.filters import Command

from handlers.dispatcher import dp

from dbmanager.insertion import insert_user


@dp.message(Command('start'))
async def start_func(message: types.Message) -> None:
    """Функция обработки команды /start"""
    kb = [
        [
            types.InlineKeyboardButton(text="О нас", callback_data="about"),
            types.InlineKeyboardButton(text="Аккаунт", callback_data="account"),
        ],
        [
            types.InlineKeyboardButton(text="Оставить отзыв", callback_data="stars"),
            types.InlineKeyboardButton(text="Контакты", callback_data="contacts"),
        ]
    ]

    insert_user(message.from_user.id, message.from_user.username)

    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await message.answer(f"Добро пожаловать {message.from_user.first_name}", reply_markup=keyboard)
