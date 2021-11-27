#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
#import os
#import subprocess

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Bienvenidos a Technocell!\nHorario: LUNES a VIERNES 9:00am - 12:00pm (COVID-19)\nPulsa sobre ayuda >> /ayuda <<')

def help(update, context):
    """Send a message when the command /help is issued."""
    menu_chat = '/ayuda Este Mensaje\n/start Bienvenida\n/Contacto # Celulares\n/Reporte\n/Solicitud\n'
    update.message.reply_text(menu_chat)

def contacto(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Tel: 47292175 Por favor llamar dos veces\nCorreo: technocell.santacruz@gmail.com\nYuniesqui Cel:+53 53327395\n')

def test(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('*_bold and italic_*', parse_mode='MarkdownV2')

def photo(update, context):
    """Send a message when the command /help is issued."""
    #filename = "/mnt/DATA/NodeServer/Main/public/meteo/last.png"
    #update.message.bot.send_photo(update.message.chat.id,open(filename,'rb'))
    update.message.reply_photo(photo=open('//mnt//DATA//NodeServer//Main//public//meteo//last.png', 'rb'))

def web(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('[Slackware](https://telete.in/iv?url=http://www.slackware.com/)', parse_mode='MarkdownV2')
    update.message.reply_text('[Slackware](https://t.me/share/url?url=https%3A%2F%2Ft.me%2Fiv%3Furl%3Dhttp%253A%252F%252Fwww.slackware.com%252F%26rhash%3D9b88308d622572)' , parse_mode='MarkdownV2')

#def server(update, context):
#    """Send a message when the command /help is issued."""
#    msg = subprocess.check_output("uname -a", shell=True)
#    update.message.reply_text(msg.decode())


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text('No entiendo: ' + update.message.text)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1157813326:AAEkOM1xQd1HjBHXxxxxxxxxxxxx", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("ayuda", help))
    dp.add_handler(CommandHandler("contacto", contacto))
    dp.add_handler(CommandHandler("test", test))
    dp.add_handler(CommandHandler("photo", photo))
    dp.add_handler(CommandHandler("web", web))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()