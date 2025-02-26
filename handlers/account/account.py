from aiogram import F, types

from handlers.dispatcher import dp


@dp.callback_query(F.data == "account")
async def account_func(callback: types.CallbackQuery) -> None:
    """Инфо об аккаунте пользователя"""
    kb = [
        [
            types.InlineKeyboardButton(text="Настроить аккаунт", callback_data="options"),
        ],
        [
            types.InlineKeyboardButton(text="Баланс", callback_data="balance"),
        ],
        [
            types.InlineKeyboardButton(text="Вернуться в меню", callback_data="menu"),

        ],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text(f"{callback.from_user.first_name} выберите действие", reply_markup=keyboard)