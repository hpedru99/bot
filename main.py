import telebot as tb
from telebot import types


token = "mytoken"
bot = tb.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Хочу!", "/help")
    bot.send_message(message.chat.id, "Привет! Меня разработал Хелкано Педру. Хочешь узнать, что я могу?",
                     reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def help_message(message):
    keyboard = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id,
                     "Я умею отвечать на эти сообщения:\n"
                     "1) Анекдот\n2) Актуальная информация\n3) Прогноз\n"
                     "И реагировать на эти команды:\n"
                     "1) /help\n2) /trust\n3) /train\n4) /response",
                     reply_markup=keyboard)


@bot.message_handler(commands=['trust'])
def trust_message(message):
    keyboard = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, "Верь мне, я всеведущ!", reply_markup=keyboard)


@bot.message_handler(commands=['train'])
def train_message(message):
    keyboard = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, "CHOOO-CHOOOO", reply_markup=keyboard)


@bot.message_handler(commands=['response'])
def response_message(message):
    keyboard = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, "О, я рад, что ты ждал моего отклика...", reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def text_message(message):
    keyboard = types.ReplyKeyboardRemove()
    if message.text.lower() == "анекдот":
        answer = "Колобок повесился"
    elif message.text.lower() == "актуальная информация":
        answer = "Уверяю, сегодня где-то что-то произошло."
    elif message.text.lower() == "прогноз":
        answer = "Над империей никогда не заходит солнце. Это точный прогноз."
    else:
        answer = "Извини, я не умею на это реагировать("
    bot.send_message(message.chat.id, answer, reply_markup=keyboard)


bot.polling(none_stop=True)
