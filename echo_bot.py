import telebot

bot = telebot.TeleBot("566724368:AAFbx-AjF0vPNrNCPitG2FDUNN6F436cjE0")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()

