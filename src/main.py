""" Module Main """
from os import getenv
from dotenv import load_dotenv
from api import FrameXAPI
from bot import TelegramBot
from launch_service import LaunchService
load_dotenv()


def main() -> None:
    """Start the telegam bot with all the requirements."""
    api = FrameXAPI()
    token_bot = getenv("TOKEN_BOT")
    launch_service = LaunchService(api)
    telebot = TelegramBot(api, token_bot, launch_service)

    telebot.bot.message_handler(commands=['start'])(telebot.send_welcome)
    telebot.bot.message_handler(commands=['help'])(telebot.send_help)
    telebot.bot.callback_query_handler(func=lambda call: True)(telebot.callback_query)
    print('Bot started correctly!')
    telebot.bot.polling(none_stop=True)

if __name__ == "__main__":
    main()
