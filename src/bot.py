""" Module TelegramBot """
import telebot
from telebot import types
from api import FrameXAPI
from launch_service import LaunchService

class TelegramBot:
    """ Class to manage the main actions of the bot """

    def __init__(self, api: FrameXAPI, token_bot: str, launch_service: LaunchService):
        self.api = api
        self.bot = telebot.TeleBot(token_bot)
        self.launch_service = launch_service

    def send_welcome(self, message: telebot.types.Message):
        """Sends a welcome message to the user who starts the chat on Telegram.

        Args:
            message (telebot.types.Message):
                Instance of the Message class from the pyTelegramBotAP library.
        """
        self.bot.reply_to(message, "Hi, this bot is a PoC")
        self.launch_service.reset_state()
        self.send_confirmation_options(message.chat.id)

    def send_help(self, message: telebot.types.Message):
        """Send help to chat in telegram using the /help

        Args:
            message (telebot.types.Message):
                Instance of the Message class from the pyTelegramBotAP library
        """
        self.bot.reply_to(message, "Hi, these are some of the options you can use /start or /help")

    def callback_query(self, call: telebot.types.CallbackQuery):
        """Executes logic to handle user responses to confirmation options.

        Args:
            call (telebot.types.CallbackQuery):
                Instance of the CallbackQuery class of the library pyTelegramBotAPI.
        """
        answer = call.data
        discard_left = answer == 'no'
        chat_id = call.message.chat.id
        self.bot.answer_callback_query(call.id, f'Answer: {answer}', cache_time=0)
        found_frame = self.launch_service.find_launch_frame(discard_left)

        if not self.launch_service.search_active:
            self.bot.reply_to(call.message, "The search process is now finished. Please send /start to start a new process.")
            return

        if found_frame:
            self.bot.reply_to(call.message, "This is the launch frame")
            self.bot.send_photo(
                chat_id=chat_id,
                photo=self.launch_service.image_url,
                caption=f'Frame: {self.launch_service.launch_frame}'
            )
            self.launch_service.reset_state()
            self.launch_service.search_active = False
            return

        self.send_confirmation_options(chat_id)

    def send_confirmation_options(self, chat_id: int):
        """Sends a message to the user with confirmation options to interact with the bot.

        Args:
            chat_id (int): ID of the Telegram chat to which the message will be sent.
        """
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn_yes = types.InlineKeyboardButton('Yes', callback_data='yes')
        btn_no = types.InlineKeyboardButton('No', callback_data='no')
        markup.add(btn_yes, btn_no)
        self.bot.send_photo(
            chat_id=chat_id,
            photo=self.launch_service.image_url,
            caption=f'Frame: {self.launch_service.current_frame}'
        )
        self.bot.send_message(chat_id, "¿Did the rocket launch yet?", reply_markup=markup)
