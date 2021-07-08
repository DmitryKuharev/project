import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from setting import TOKEN

updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello")


def echo(update, context):
    text = "Я повторяю: " + update.message.text
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)


start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)

updater.start_polling()

