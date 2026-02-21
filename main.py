from keyboard import markup
from config import bot
from logic import get_schedule

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
    bot.send_message(call.message.chat.id, f"📅 Вот расписание уроков!\n{get_schedule()}")

@bot.callback_query_handler(func=lambda call: call.data == "about")
def callback_schedule(call):
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, "ℹ️ О нашей школе!\n🏫 Добро пожаловать в нашу школу «Светлый путь»!\n\n"
    "📚 Здесь учатся самые любознательные ученики и раскрываются таланты каждого.\n"
    "👩‍🏫 Наши преподаватели — настоящие профессионалы, которые любят своё дело.\n"
    "🎨 В школе есть кружки по искусству, робототехнике, спорту и музыке.\n"
    "🌿 У нас уютный двор, современные классы и библиотека с интересными книгами.\n"
    "✨ Мы создаём атмосферу, где каждый ученик чувствует себя важным и особенным!")

@bot.callback_query_handler(func=lambda call: call.data == "teachers")
def callback_teachers(call):
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id,"Вот ссылка на таблицу https://docs.google.com/spreadsheets/d/1OLZY0EnwS59UpVyjVvsOhnEllgaGHH1mQALu4gkOdu4/edit?usp=sharing")



bot.polling()