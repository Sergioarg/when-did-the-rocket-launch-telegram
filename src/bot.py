from os import getenv
from dotenv import load_dotenv
import telebot
from telebot import types

load_dotenv()
URL = 'https://framex-dev.wadrid.net/api/video/Falcon%20Heavy%20Test%20Flight%20(Hosted%20Webcast)-wbSwFU6tY1c/frame/600/'
URL_2 = 'https://framex-dev.wadrid.net/api/video/Falcon%20Heavy%20Test%20Flight%20(Hosted%20Webcast)-wbSwFU6tY1c/frame/800/'

TOKEN_BOT = getenv("TOKEN_BOT")

def init_bot():
    bot = telebot.TeleBot(TOKEN_BOT)
    return bot

def send_welcome(message):
    bot.reply_to(message, "Hola, esto es una prueba con Telebot")

def send_help(message):
    bot.reply_to(message, "Este es el comando de HELP")

def send_options(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn_yes = types.InlineKeyboardButton('Yes', callback_data='yes')
    btn_no = types.InlineKeyboardButton('No', callback_data='no')
    markup.add(btn_yes, btn_no)
    bot.send_message(message.chat.id, "Did the rocket launch yet?", reply_markup=markup)
    send_image(message.chat.id, 'https://framex-dev.wadrid.net/api/video/Falcon%20Heavy%20Test%20Flight%20(Hosted%20Webcast)-wbSwFU6tY1c/frame/600/', 'Imagen test')

def send_image(chat_id, url, caption):
    bot.send_photo(chat_id=chat_id, photo=url, caption=caption)

def callback_query(call):
    if call.data == 'yes':
        bot.answer_callback_query(call.id, 'Answer: YES')
        send_image(call.message.chat.id, URL, 'test')
        send_confirmation_options(call.message.chat.id)
    elif call.data == 'no':
        bot.answer_callback_query(call.id, 'Answer: NO')
        send_image(call.message.chat.id, URL_2, 'otra')
        send_confirmation_options(call.message.chat.id)

def send_confirmation_options(chat_id):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn_yes = types.InlineKeyboardButton('Yes', callback_data='confirm_yes')
    btn_no = types.InlineKeyboardButton('No', callback_data='confirm_no')
    markup.add(btn_yes, btn_no)
    bot.send_message(chat_id, "¿Did the rocket launch yet?", reply_markup=markup)

if __name__ == "__main__":
    print("Bot iniciado correctamente!")
    bot = init_bot()
    bot.message_handler(commands=['start'])(send_welcome)
    bot.message_handler(commands=['help'])(send_help)
    bot.message_handler(commands=['launch'])(send_options)
    bot.callback_query_handler(func=lambda call: True)(callback_query)
    bot.polling(none_stop=True)
