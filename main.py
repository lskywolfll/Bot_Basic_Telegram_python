from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from gtts import gTTS
import json
import requests
import random
from proverb.proverb import get_proverb as get_scraping_proverb


updater = Updater(
    "your token telegram", use_context=True)

def scraping_proverb_aleatory(update: Update, context: CallbackContext):
    command = "proverb_scraping_aleatory"
    proverb = get_scraping_proverb()
    create_voice_recorded(proverb, "es", command)
    update.message.reply_voice(open(f"{command}.mp3", "rb"))

def get_proverb():
    response = requests.get("http://localhost:3000/proverb")
    proverbs = json.loads(response.content)
    return random.choice(proverbs)


def proverb_aleatory(update: Update, context: CallbackContext):
    command = "proverb_aleatory"
    proverb = get_proverb()
    text = f"{proverb['content']} escrito por {proverb['author']}"
    create_voice_recorded(text, "es", command)
    update.message.reply_voice(open(f"{command}.mp3", "rb"))


def create_voice_recorded(txt: str, lang: str, command: str):
    recorded = gTTS(text=txt, lang=lang, slow=True, tld='es')
    recorded.save(f"{command}.mp3")


def start(update: Update, context: CallbackContext):
    text = "Hola bienvenido o bienvenida al bot de bei luo"
    command = "start"
    create_voice_recorded(text, "es", command)
    update.message.reply_voice(open(f"{command}.mp3", "rb"))


def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
    /youtube - To get the youtube URL
    /linkedin - To get the LinkedIn profile URL
    /gmail - To get gmail URL
    /geeks - To get the GeeksforGeeks URL
    /proverb - to get aleatory proverb scraping""")


def gmail_url(update: Update, context: CallbackContext):
    update.message.reply_text("prueba@gmail.com")


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
updater.dispatcher.add_handler(CommandHandler('proverb', scraping_proverb_aleatory))
updater.dispatcher.add_handler(CommandHandler(
    'proverb_aleatory', proverb_aleatory))

updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
    # Filters out unknown commands
    Filters.command, unknown))

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
