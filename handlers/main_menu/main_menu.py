from aiogram import types, F

from handlers.dispatcher import dp


@dp.callback_query(F.data == "menu")
async def start_func(callback: types.CallbackQuery) -> None:
    """Главное меню"""
    kb = [
        [
            types.InlineKeyboardButton(text="О нас", callback_data="about"),
            types.InlineKeyboardButton(text="Аккаунт", callback_data="account"),
        ],
        [
            types.InlineKeyboardButton(text="Оставить отзыв", callback_data="review"),
            types.InlineKeyboardButton(text="Контакты", callback_data="contacts"),
        ]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text(f"Добро пожаловать {callback.from_user.first_name}", reply_markup=keyboard)
