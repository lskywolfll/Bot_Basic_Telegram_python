from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters


updater = Updater("your token telegram bot",
                  use_context=True)


def start(update: Update, context: CallbackContext):
    text = "Hola! bienvenido/a al bot de bei luo"
    update.message.reply_text(text)


def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
    /youtube - To get the youtube URL
    /linkedin - To get the LinkedIn profile URL
    /gmail - To get gmail URL
    /geeks - To get the GeeksforGeeks URL""")


def gmail_url(update: Update, context: CallbackContext):
    update.message.reply_text("jiaox1577@gmail.com")


def youtube_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "https://www.youtube.com/channel/UCujboKM-OsjNig3WoRxjRKA/featured")


def linkedIn_url(update: Update, context: CallbackContext):
    update.message.reply_text("www.linkedin.com/in/rené-alejandro-s-764379172")


def geeks_url(update: Update, context: CallbackContext):
    update.message.reply_text("GeeksforGeeks url here")


def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Lo sentimos no puedo entender , lo que has dicho '%s'" % update.message.text)


def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Lo siento '%s' no es un comando valido" % update.message.text)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('youtube', youtube_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('linkedin', linkedIn_url))
updater.dispatcher.add_handler(CommandHandler('gmail', gmail_url))
updater.dispatcher.add_handler(CommandHandler('geeks', geeks_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
    # Filters out unknown commands
    Filters.command, unknown))

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()