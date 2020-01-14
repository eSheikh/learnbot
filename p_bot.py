from telegram.ext import Updater, CommandHandler
import logging


logging.basicConfig(format = '%(name)s - %(levelname)s - %(message)s - %(asctime)s',
                    level = logging.INFO,
                    filename = 'bot.log'
                    )

def start(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

    
def main():
    mybot = Updater("566724368:AAFbx-AjF0vPNrNCPitG2FDUNN6F436cjE0", use_context=True)
    
    logging.info('Бот запускается')
    
    mybot.dispatcher.add_handler(CommandHandler('start',start))
    
    mybot.start_polling()
    mybot.idle()


main()
