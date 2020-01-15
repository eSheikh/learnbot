from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent
import logging


logging.basicConfig(format = '%(name)s - %(levelname)s - %(message)s - %(asctime)s',
                    level = logging.INFO,
                    filename = 'bot.log'
                    )
def main():
    mybot = Updater("566724368:AAFbx-AjF0vPNrNCPitG2FDUNN6F436cjE0", use_context=True)
    
    logging.info('Бот запускается')
    
    mybot.dispatcher.add_handler(CommandHandler('start', start))
    mybot.dispatcher.add_handler(MessageHandler(Filters.text, echo))
    mybot.dispatcher.add_handler(CommandHandler('caps', caps))
    mybot.dispatcher.add_handler(InlineQueryHandler(inline_caps))
    mybot.dispatcher.add_handler(MessageHandler(Filters.command, unknown))
    
    mybot.start_polling()
    mybot.idle()


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет")

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

def inline_caps(update, context):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id = query.upper(),
            title = 'Caps',
            input_message_content = InputMessageContent(query.upper())
            )
        )
    context.bot.answer_inline_query(update.inline_query.id, results)

def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Неизвсетная команда")


main()
