from aiogram import F, types

from handlers.dispatcher import dp


@dp.callback_query(F.data == "options")
async def options_func(callback: types.CallbackQuery) -> None:
    kb = [
        [
            types.InlineKeyboardButton(text="Изменить номер телефона", callback_data="change_number")
        ],
        [
            types.InlineKeyboardButton(text="Изменить язык", callback_data="change_language")
        ],
        [
            types.InlineKeyboardButton(text="Назад", callback_data="account"),
            types.InlineKeyboardButton(text="В главное меню", callback_data="menu"),
        ]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text("Выберите действие", reply_markup=keyboard)