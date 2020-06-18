from telegram import KeyboardButton, ReplyKeyboardMarkup

BUTTON1_LAST_RECORD = "Last record"

def get_base_reply_keyboard():
    keyboard = [
        [
            KeyboardButton(BUTTON1_LAST_RECORD),
        ],
    ]
    return ReplyKeyboardMarkup(
        keyboard = keyboard,
        resize_keyboard = True,
    )