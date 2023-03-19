import socket
import os

import telebot
# token = '6148577713:AAEMqW4wBgGw57wTYBMkJkFnpc8OIBjD-_g'
token = os.environ['TOKEN']
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message: telebot.types.Message):
    bot.send_message(message.from_user.id, 'Я работаю автономно , я сбежал !!!!')
bot.infinity_polling()
