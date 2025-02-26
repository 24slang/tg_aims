from aiogram import F, types

from handlers.dispatcher import dp


@dp.callback_query(F.data == "contacts")
async def contacts_func(callback: types.CallbackQuery) -> None:
    kb = [
        [
            types.InlineKeyboardButton(text="Написать нам", callback_data="to_message"),
            types.InlineKeyboardButton(text="Назад", callback_data="menu"),
        ],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text("Номер телефона:\n+375336193565", reply_markup=keyboard)