from os import getenv
from dotenv import load_dotenv
import telebot
from telebot import types

load_dotenv()
URL = 'https://framex-dev.wadrid.net/api/video/Falcon%20Heavy%20Test%20Flight%20(Hosted%20Webcast)-wbSwFU6tY1c/frame/600/'
URL_2 = 'https://framex-dev.wadrid.net/api/video/Falcon%20Heavy%20Test%20Flight%20(Hosted%20Webcast)-wbSwFU6tY1c/frame/800/'

TOKEN_BOT = getenv("TOKEN_BOT")

class TelegramBot:
    def __init__(self):
        self.bot = telebot.TeleBot(TOKEN_BOT)

    def send_welcome(self, message):
        self.bot.reply_to(message, "Hola, esto es una prueba con Telebot")

    def send_help(self, message):
        self.bot.reply_to(message, "Este es el comando de HELP")

    def send_options(self, message):
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn_yes = types.InlineKeyboardButton('Yes', callback_data='yes')
        btn_no = types.InlineKeyboardButton('No', callback_data='no')
        markup.add(btn_yes, btn_no)
        self.bot.send_message(message.chat.id, "Did the rocket launch yet?", reply_markup=markup)
        self.send_image(message.chat.id, 'https://framex-dev.wadrid.net/api/video/Falcon%20Heavy%20Test%20Flight%20(Hosted%20Webcast)-wbSwFU6tY1c/frame/600/', 'Imagen test')

    def send_image(self, chat_id, url, caption):
        self.bot.send_photo(chat_id=chat_id, photo=url, caption=caption)

    def callback_query(self, call):
        if call.data == 'yes':
            self.bot.answer_callback_query(call.id, 'Answer: YES')
            self.send_image(call.message.chat.id, URL, 'test')
            self.send_confirmation_options(call.message.chat.id)
        elif call.data == 'no':
            self.bot.answer_callback_query(call.id, 'Answer: NO')
            self.send_image(call.message.chat.id, URL_2, 'otra')
            self.send_confirmation_options(call.message.chat.id)

    def send_confirmation_options(self, chat_id):
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn_yes = types.InlineKeyboardButton('Yes', callback_data='confirm_yes')
        btn_no = types.InlineKeyboardButton('No', callback_data='confirm_no')
        markup.add(btn_yes, btn_no)
        self.bot.send_message(chat_id, "¿Did the rocket launch yet?", reply_markup=markup)
