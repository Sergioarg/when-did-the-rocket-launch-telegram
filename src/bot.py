from os import getenv
from dotenv import load_dotenv
import telebot
from telebot import types

load_dotenv()

# temp code
from api import FrameXAPI
import random
api = FrameXAPI()

# Generar un número aleatorio entre 1 y 100
random_frame = random.randint(35500, 39568)
temp_img = api.get_link_frame(random_frame)


TOKEN_BOT = getenv("TOKEN_BOT")

class TelegramBot:
    def __init__(self):
        self.bot = telebot.TeleBot(TOKEN_BOT)

    def send_welcome(self, message):
        self.bot.reply_to(message, "Hi, this bot is a PoC, here are the options you can use")
        self.send_menu_options(message)

    def send_help(self, message):
        self.bot.reply_to(message, "Hello these are some of the options you can use")
        self.send_menu_options(message)

    def send_menu_options(self, message):
        markup = types.InlineKeyboardMarkup(row_width=3)
        btn_start = types.InlineKeyboardButton('Start', callback_data='start')
        btn_launch = types.InlineKeyboardButton('Launch', callback_data='launch')
        btn_help = types.InlineKeyboardButton('Help', callback_data='help')
        markup.add(btn_start, btn_launch, btn_help)
        self.bot.send_message(message.chat.id, "Choose an action:", reply_markup=markup)

    def callback_query(self, call):
        chat_id = call.message.chat.id

        if call.data == 'start':
            self.send_welcome(call.message)
        elif call.data == 'launch':
            self.send_confirmation_options(chat_id)
        elif call.data == 'help':
            self.send_help(call.message)

        if call.data == 'yes':
            print("YES!")
            self.bot.answer_callback_query(call.id, 'Answer: YES', cache_time=0)
            self.send_confirmation_options(chat_id)
        if call.data == 'no':
            print("NO!")
            self.bot.answer_callback_query(call.id, 'Answer: NO', cache_time=0)
            self.send_confirmation_options(chat_id)

    def send_confirmation_options(self, chat_id):
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn_yes = types.InlineKeyboardButton('Yes', callback_data='yes')
        btn_no = types.InlineKeyboardButton('No', callback_data='no')
        markup.add(btn_yes, btn_no)
        self.bot.send_photo(chat_id, photo=temp_img, caption=f'Frame: {random_frame}')
        self.bot.send_message(chat_id, "¿Did the rocket launch yet?", reply_markup=markup)
