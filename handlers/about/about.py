from aiogram import F, types

from handlers.dispatcher import dp


@dp.callback_query(F.data == "about")
async def about_func(callback: types.CallbackQuery) -> None:
    """О нас"""
    kb = [
        [
            types.InlineKeyboardButton(text="Вернуться в меню", callback_data="menu")
        ]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text("О нас пока что пусто но мы над этим работаем", reply_markup=keyboard)
