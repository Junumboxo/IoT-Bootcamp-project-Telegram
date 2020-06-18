#!/usr/bin/python3.8
# -*- coding: utf-8 -*-

from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from config import TG_TOKEN
from reply_buttons import BUTTON_LAST_RECORD, get_base_reply_keyboard

TITLES = { "INLINE_BUTTON_GOOD": '👌', "INLINE_BUTTON_BAD": '😨'}

CALLBACK_BUTTON_GOOD = "callback_button_good"
CALLBACK_BUTTON_BAD = "callback_button_bad"

def get_base_inline_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(TITLES["INLINE_BUTTON_GOOD"], callback_data = CALLBACK_BUTTON_GOOD),
            InlineKeyboardButton(TITLES["INLINE_BUTTON_BAD"], callback_data = CALLBACK_BUTTON_BAD),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)

def keyboard_callback_handler(bot, update, chat_data = None, **kwargs):
    query = update.callback_query
    data = query.data

    chat_id = update.effective_message.chat_id

    if data == CALLBACK_BUTTON_GOOD:
        #we should obligotary update the database with the data about health
        bot.send_message(
            chat_id = chat_id,
            text = "Glad youre OK!",
            reply_markup = get_base_reply_keyboard(),
        )
        
    elif data == CALLBACK_BUTTON_BAD:
        bot.send_message(
            chat_id = chat_id,
            text = "OK, sorry, go have some tea",
            reply_markup = get_base_reply_keyboard(),   
        )
        

def do_start(bot, update):
    bot.send_message(
        chat_id = update.message.chat_id,
        text = "Hi",
    )

def do_echo(bot, update):
    text = update.message.text
    if text == "feel": 
        #ideally we should ask for health if we have a row in a database without data about health, but for now let it be like this
        bot.send_message(
            chat_id = update.message.chat_id,
            text = "How do you feel?",
            reply_markup = get_base_inline_keyboard(),
        )
    else:
        if text == BUTTON_LAST_RECORD:
            reply = "t = 27, h = 50" #later we will get this data from the database
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
    buttons_handler = CallbackQueryHandler(callback = keyboard_callback_handler, pass_chat_data = True)

    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(message_handler)
    updater.dispatcher.add_handler(buttons_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()