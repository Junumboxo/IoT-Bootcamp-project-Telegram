#!/usr/bin/python3.8
# -*- coding: utf-8 -*-

from logging import getLogger
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from reply_buttons import BUTTON_LAST_RECORD, BUTTON_HELP, BUTTON_FEEL, get_base_reply_keyboard
from msg_buttons import CALLBACK_BUTTON_GOOD, CALLBACK_BUTTON_BAD, get_base_inline_keyboard
from msg_texts import msg_start, msg_help, msg_echo, msg_feel_GOOD, msg_fell_BAD

from config import load_config
from utils import logger_factory

config = load_config()
logger = getLogger(__name__)    
debug_requests = logger_factory(logger=logger)

@debug_requests
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

@debug_requests
def do_start(bot, update):
    bot.send_message(
        chat_id = update.message.chat_id,
        text = msg_start,
    )

@debug_requests
def do_help(bot, update):
    bot.send_message(
        chat_id = update.message.chat_id,
        text = msg_help,
        reply_markup = get_base_reply_keyboard(),
    )

#ideally we should ask for health if we have a row in a database without data about health, but for now let it be like this
@debug_requests
def do_feel(bot, update):
    bot.send_message(
        chat_id = update.message.chat_id,
        text = "How do you feel?",
        reply_markup = get_base_inline_keyboard(),
    )

#here we will have to optimize the code when we get access to the database
@debug_requests
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
    logger.info("The bot is starting...")
    bot = Bot(
        token = config.TG_TOKEN,   
    )
    updater = Updater(
        bot = bot,
    )

    #Check if bot found TG API
    info = bot.get_me()
    logger.info(f'Bot info: {info}')

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