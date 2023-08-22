import telebot
from telebot import types

TOKEN = "TG_BOT_TOKEN"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(
        "Посмотреть фото", callback_data="photos"))
    keyboard.add(types.InlineKeyboardButton(
        "Узнать о увлечении", callback_data="hobby"))
    keyboard.add(types.InlineKeyboardButton(
        "Послушать войсы", callback_data="voices"))
    bot.send_message(message.chat.id, "Привет!")
    bot.send_message(
        message.chat.id, "Используй команду /github для получения ссылки на репозиторий")
    bot.send_message(
        message.chat.id, "Что бы вы хотели узнать?", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'photos')
def photos_menu(call):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("Селфи", callback_data="selfie"))
    keyboard.add(types.InlineKeyboardButton(
        "Фото из старшей школы", callback_data="school"))
    keyboard.add(types.InlineKeyboardButton("Назад", callback_data="main"))
    bot.edit_message_text("Какое фото вы хотите посмотреть?", chat_id=call.message.chat.id,
                          message_id=call.message.message_id, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'hobby')
def hobby_menu(call):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("Назад", callback_data="main"))
    bot.send_message(call.message.chat.id,
                     "Небольшой рассказ о себе. Я скромный человек, очень сромный :)", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'voices')
def voices_menu(call):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(
        "Что такое GPT", callback_data="gpt"))
    keyboard.add(types.InlineKeyboardButton(
        "Разницу между SQL и NoSQL", callback_data="nosql"))
    keyboard.add(types.InlineKeyboardButton("Назад", callback_data="main"))
    bot.edit_message_text("О чем вы хотите услышать?", chat_id=call.message.chat.id,
                          message_id=call.message.message_id, reply_markup=keyboard)


@bot.message_handler(commands=['github'])
def send_github(message):
    bot.send_message(message.chat.id,
                     "<a href='https://github.com/Edifiels/TG_Bot_test'>github</a>", parse_mode="HTML")


@bot.callback_query_handler(func=lambda call: call.data in ['gpt', 'nosql'])
def send_voice(call):
    if call.data == 'gpt':
        bot.send_voice(chat_id=call.message.chat.id,
                       voice=open("media/voice/first.ogg", "rb"))
    elif call.data == 'nosql':
        bot.send_voice(chat_id=call.message.chat.id, voice=open(
            "media/voice/two.ogg", "rb"))


@bot.callback_query_handler(func=lambda call: call.data in ['selfie', 'school'])
def send_photo(call):
    if call.data == 'selfie':
        bot.send_photo(chat_id=call.message.chat.id,
                       photo=open("media/photo/selfie.jpg", "rb"))
    elif call.data == 'school':
        bot.send_photo(chat_id=call.message.chat.id, photo=open(
            "media/photo/school_photo.jpg", "rb"))


@bot.callback_query_handler(func=lambda call: call.data == 'main')
def main_menu(call):
    send_welcome(call.message)


if __name__ == '__main__':
    bot.polling(non_stop=True)
