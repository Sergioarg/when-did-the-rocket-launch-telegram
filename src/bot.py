from os import getenv
from dotenv import load_dotenv
import telebot
from telebot import types

load_dotenv()

TOKEN_BOT = getenv("TOKEN_BOT")

print(TOKEN_BOT)

bot = telebot.TeleBot(TOKEN_BOT)

URL = 'https://framex-dev.wadrid.net/api/video/Falcon%20Heavy%20Test%20Flight%20(Hosted%20Webcast)-wbSwFU6tY1c/frame/600/'
URL_2 = 'https://framex-dev.wadrid.net/api/video/Falcon%20Heavy%20Test%20Flight%20(Hosted%20Webcast)-wbSwFU6tY1c/frame/800/'

# Creacion de comandos simples como 'start' y 'help'

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hola, esto es una prueba con Telebot")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Este es el comando de HELP")



@bot.message_handler(commands=['launch'])
def send_options(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    # Creacion de botones

    btn_yes = types.InlineKeyboardButton('Yes', callback_data='yes')
    btn_no = types.InlineKeyboardButton('No', callback_data='no')
    markup.add(btn_yes, btn_no)

    bot.send_message(message.chat.id, "Did the rocket launch yet?", reply_markup=markup)
    # Send image
    url = 'https://framex-dev.wadrid.net/api/video/Falcon%20Heavy%20Test%20Flight%20(Hosted%20Webcast)-wbSwFU6tY1c/frame/600/'
    bot.send_photo(chat_id=message.chat.id, photo=url, caption='Imagen test')


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'yes':
        # TODO: Send other image
        bot.answer_callback_query(call.id, 'Answer: YES')
        bot.send_photo(chat_id=call.message.chat.id, photo=URL, caption='test')
        # markup
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn_yes = types.InlineKeyboardButton('Yes', callback_data='confirm_yes')
        btn_no = types.InlineKeyboardButton('No', callback_data='confirm_no')
        markup.add(btn_yes, btn_no)


        bot.send_message(call.message.chat.id, "¿Did the rocket launch yet?", reply_markup=markup)
        bot.send_photo(chat_id=call.message.chat.id, photo=URL, caption='otra')

    elif call.data == 'no':
        # TODO: Send other image
        bot.answer_callback_query(call.id, 'Answer: NO')

        markup = types.InlineKeyboardMarkup(row_width=2)
        btn_yes = types.InlineKeyboardButton('Yes', callback_data='confirm_yes')
        btn_no = types.InlineKeyboardButton('No', callback_data='confirm_no')
        markup.add(btn_yes, btn_no)

        new_image_url = URL_2
        bot.send_message(call.message.chat.id, "¿Did the rocket launch yet?", reply_markup=markup)
        bot.send_photo(chat_id=call.message.chat.id, photo=new_image_url, caption='otra')

if __name__ == "__main__":
    print("Bot iniciado correctamente!")
    bot.polling(none_stop=True)
