from bot import TelegramBot

def main():
    telebot = TelegramBot()
    telebot.bot.message_handler(commands=['start'])(telebot.send_welcome)
    telebot.bot.message_handler(commands=['help'])(telebot.send_help)
    telebot.bot.message_handler(commands=['launch'])(telebot.send_options)
    telebot.bot.callback_query_handler(func=lambda call: True)(telebot.callback_query)
    print('Bot iniciado correctamente.')
    telebot.bot.polling(none_stop=True)

if __name__ == "__main__":
    main()
