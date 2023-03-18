import socket
import os

import telebot
# token = '6148577713:AAEMqW4wBgGw57wTYBMkJkFnpc8OIBjD-_g'
token = os.environ['TOKEN']
bot = telebot.TeleBot(token)

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind(('localhost', 666))


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message: telebot.types.Message):
    bot.send_message(message.from_user.id, 'Я работаю автономно , кля !!!!')
bot.infinity_polling()
