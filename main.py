import telebot
from keyboard import markup

bot = telebot.TeleBot("8481708525:AAEjJX4kcY8YQh5kpDJtvu4NFUEehIri684")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "👋 Привет!\n\n"
        "🎓 Добро пожаловать в онлайн-школу!\n\n"
        "📚 Здесь ты сможешь:\n"
        "• смотреть расписание уроков\n"
        "• получать важные обновления\n"
        "• быть в курсе всех событий\n\n"
        "Готов начать? 🚀",
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: call.data == "schedule")
def callback_schedule(call):
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, "📅 Вот расписание уроков!")

@bot.callback_query_handler(func=lambda call: call.data == "about")
def callback_schedule(call):
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, "ℹ️ О нашей школе!")

bot.polling()