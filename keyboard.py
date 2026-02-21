from telebot import types

markup = types.InlineKeyboardMarkup(row_width=2)

markup.add(
    types.InlineKeyboardButton("📅 Расписание", callback_data="schedule"),
    types.InlineKeyboardButton("ℹ️ О школе", callback_data="about"),
    types.InlineKeyboardButton("ℹ️ Для учителей", callback_data="teachers")
)