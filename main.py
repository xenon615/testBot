
import telebot
import json
token = '6148577713:AAEMqW4wBgGw57wTYBMkJkFnpc8OIBjD-_g'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message: telebot.types.Message):
    bot.send_message(message.from_user.id, 'echo')



bot.infinity_polling()
