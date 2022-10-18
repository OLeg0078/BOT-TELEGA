from email import message
import telebot
bot = telebot.TeleBot('5559896717:AAF-GxltGSmIaTn3iGiL8CyHr8KSXIMQoZM')

@bot.message_handler(commands=['start'])
def start(message):
     bot.send_message(message.chat.id, '<b>Привет</b>' , parse_mode = 'html')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
     if message.text.lower() == "привет":
          bot.send_message(message.chat.id, '<b>Пошёл нахуй!</b>' , parse_mode = 'html')

bot.polling(none_stop=True)