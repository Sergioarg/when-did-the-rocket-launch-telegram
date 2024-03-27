import telebot
from telebot import types
class TelegramBot:
    def __init__(self, api, token_bot, launch_service):
        self.api = api
        self.bot = telebot.TeleBot(token_bot)
        self.launch_service = launch_service

    def send_welcome(self, message):
        self.bot.reply_to(message, "Hi, this bot is a PoC")
        self.send_confirmation_options(message.chat.id)

    def send_help(self, message):
        self.bot.reply_to(message, "Hi, these are some of the options you can use /start y /help")
        self.send_menu_options(message)

    def send_menu_options(self, message):
        markup = types.InlineKeyboardMarkup(row_width=3)
        btn_start = types.InlineKeyboardButton('Start', callback_data='start')
        btn_launch = types.InlineKeyboardButton('Launch', callback_data='launch')
        btn_help = types.InlineKeyboardButton('Help', callback_data='help')
        markup.add(btn_start, btn_launch, btn_help)
        self.bot.send_message(message.chat.id, "Choose an action:", reply_markup=markup)

    def callback_query(self, call):

        answer = call.data
        discard_left = answer == 'no'
        chat_id = call.message.chat.id
        self.bot.answer_callback_query(call.id, f'Answer: {answer}', cache_time=0)
        found_frame = self.launch_service.find_launch_frame(discard_left)

        if found_frame:
            self.bot.reply_to(call.message, "This is the lauch frame")
            self.bot.send_photo(chat_id, photo=self.launch_service.image_url, caption=f'Frame: {self.launch_service.launch_frame}')
            return

        self.send_confirmation_options(chat_id)

    def send_confirmation_options(self, chat_id):
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn_yes = types.InlineKeyboardButton('Yes', callback_data='yes')
        btn_no = types.InlineKeyboardButton('No', callback_data='no')
        markup.add(btn_yes, btn_no)
        self.bot.send_photo(chat_id, photo=self.launch_service.image_url, caption=f'Frame: {self.launch_service.current_frame}')
        self.bot.send_message(chat_id, "¿Did the rocket launch yet?", reply_markup=markup)
