#!/usr/bin/python3.8
# -*- coding: utf-8 -*-

from logging import getLogger
from telegram import Bot, Update, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from reply_buttons import BUTTON_LAST_RECORD, BUTTON_HELP, BUTTON_FEEL, get_base_reply_keyboard
from msg_buttons import CALLBACK_BUTTON_GOOD, CALLBACK_BUTTON_BAD, CALLBACK_BUTTON_SEND, CALLBACK_BUTTON_DISCARD, get_inline_keyboard_health, get_inline_keyboard_confirm
from msg_texts import msg_start, msg_help, msg_echo, msg_feel, msg_feel_GOOD, msg_feel_BAD, msg_feel_SEND, msg_feel_DISCARD

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
        bot.send_message(
            chat_id = chat_id,
            text = msg_feel_GOOD,
            reply_markup = get_inline_keyboard_confirm(),
        )
    elif data == CALLBACK_BUTTON_BAD:
        bot.send_message(
            chat_id = chat_id,
            text = msg_feel_BAD,
            reply_markup = get_inline_keyboard_confirm(),   
        )
    elif data == CALLBACK_BUTTON_SEND:
        bot.send_message(
            chat_id = chat_id,
            text = msg_feel_SEND,
            reply_markup = get_base_reply_keyboard(),   
        )
        #here we have to send the data to the server

    elif data == CALLBACK_BUTTON_DISCARD:
        bot.send_message(
            chat_id = chat_id,
            text = msg_feel_DISCARD,  
        )
        do_feel(bot, update, chat_id)

@debug_requests
def do_start(bot, update):
    chat_id = update.effective_message.chat_id
    bot.send_message(
        chat_id = chat_id,
        text = msg_start,
        parse_mode = ParseMode.HTML,
        reply_markup = get_base_reply_keyboard(),
    )

@debug_requests
def get_last_record(bot, update, chat_id):
    #later we will get this data from the database
    #and we will have to check these values on thresholds
    datetime = "Current datetime"
    temperature = 27.67
    humidity = 55.00

    reply = 'Datetime of measurements - {},\nTemperature - {} °C,\nHumidity - {} %'.format(datetime, temperature, humidity)
    bot.send_message(
        chat_id = chat_id,
        text = reply,
        reply_markup = get_base_reply_keyboard(),
    )

@debug_requests
def do_help(bot, update, chat_id):
    bot.send_message(
        chat_id = chat_id,
        text = msg_help,
        parse_mode = ParseMode.HTML,
        reply_markup = get_base_reply_keyboard(),
    )

#ideally we should ask for health if we have a row in a database without data about health, but for now let it be like this
@debug_requests
def do_feel(bot, update, chat_id):
    bot.send_message(
        chat_id = chat_id,
        text = msg_feel,
        reply_markup = get_inline_keyboard_health(),
    )

@debug_requests
def do_echo(bot, update):
    chat_id = update.effective_message.chat_id
    text = update.message.text

    if text == BUTTON_LAST_RECORD:
        get_last_record(bot, update, chat_id)
    elif text == BUTTON_HELP:
        do_help(bot, update, chat_id)
    elif text == BUTTON_FEEL:
        do_feel(bot, update, chat_id)
    else:
        reply = msg_echo
        bot.send_message(
            chat_id = chat_id,
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
    message_handler = MessageHandler(Filters.text, do_echo)
    buttons_handler = CallbackQueryHandler(callback = keyboard_callback_handler, pass_chat_data = True)

    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(message_handler)
    updater.dispatcher.add_handler(buttons_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()