from aiogram import F, types

from handlers.dispatcher import dp


@dp.callback_query(F.data == "balance")
async def balance_func(callback: types.CallbackQuery) -> None:
    kb = [
        [
            types.InlineKeyboardButton(text="Пополнить баланс", callback_data="balance_refill"),
        ],
        [
            types.InlineKeyboardButton(text="В главное меню", callback_data="menu"),
            types.InlineKeyboardButton(text="Назад", callback_data="account"),
        ]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text("Ваш баланс:\n\n 930 BYN. ", reply_markup=keyboard)