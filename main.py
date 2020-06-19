#!/usr/bin/python3.8
# -*- coding: utf-8 -*-

from telegram import Bot, Update#, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from config import TG_TOKEN
from reply_buttons import BUTTON_LAST_RECORD, BUTTON_HELP, BUTTON_FEEL, get_base_reply_keyboard
from msg_buttons import CALLBACK_BUTTON_GOOD, CALLBACK_BUTTON_BAD, get_base_inline_keyboard
from msg_texts import msg_start, msg_help, msg_echo, msg_feel_GOOD, msg_fell_BAD

def keyboard_callback_handler(bot, update, chat_data = None, **kwargs):
    query = update.callback_query
    data = query.data

    chat_id = update.effective_message.chat_id

    if data == CALLBACK_BUTTON_GOOD:
        #we should obligotary update the database with the data about health
        bot.send_message(
            chat_id = chat_id,
            text = msg_feel_GOOD,
            reply_markup = get_base_reply_keyboard(),
        )
        
    elif data == CALLBACK_BUTTON_BAD:
        bot.send_message(
            chat_id = chat_id,
            text = msg_fell_BAD,
            reply_markup = get_base_reply_keyboard(),   
        )

def do_start(bot, update):
    bot.send_message(
        chat_id = update.message.chat_id,
        text = msg_start,
    )

def do_help(bot, update):
    bot.send_message(
        chat_id = update.message.chat_id,
        text = msg_help,
        reply_markup = get_base_reply_keyboard(),
    )

#ideally we should ask for health if we have a row in a database without data about health, but for now let it be like this
def do_feel(bot, update):
    bot.send_message(
        chat_id = update.message.chat_id,
        text = "How do you feel?",
        reply_markup = get_base_inline_keyboard(),
    )

#here we will have to optimize the code when we get access to the database
def do_echo(bot, update):
    text = update.message.text
    if text == BUTTON_LAST_RECORD:
        reply = "t = 27, h = 50" #later we will get this data from the database
        bot.send_message(
            chat_id = update.message.chat_id,
            text = reply,
            reply_markup = get_base_reply_keyboard(),
        )
    elif text == BUTTON_HELP:
        do_help(bot, update)
    elif text == BUTTON_FEEL:
        do_feel(bot, update)
    else:
        reply = msg_echo
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
    help_handler = CommandHandler("help", do_help)
    message_handler = MessageHandler(Filters.text, do_echo)
    buttons_handler = CallbackQueryHandler(callback = keyboard_callback_handler, pass_chat_data = True)

    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(help_handler)
    updater.dispatcher.add_handler(message_handler)
    updater.dispatcher.add_handler(buttons_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()