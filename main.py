#!/usr/bin/python3.8

from telegram import Bot
from telegram import Update

from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters

from config import TG_TOKEN
from buttons import BUTTON1_LAST_RECORD, get_base_reply_keyboard

def do_start(bot: Bot, update: Update):
    bot.send_message(
        chat_id = update.message.chat_id,
        text = "Hi",
    )

def do_echo(bot: Bot, update: Update):
    text = update.message.text
    if text == BUTTON1_LAST_RECORD:
        reply = "t = 27, h = 50"
    else:
        reply = "Dont understand"
    bot.send_message(
        chat_id = update.message.chat_id,
        text = reply,
        reply_markup = get_base_reply_keyboard(),
    )
def main():
    bot = Bot(
        token = TG_TOKEN,   
    )
    updater = Updater(
        bot = bot,
    )

    start_handler = CommandHandler("start", do_start)
    message_handler = MessageHandler(Filters.text, do_echo)

    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(message_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()