from telegram import KeyboardButton, ReplyKeyboardMarkup

BUTTON_LAST_RECORD = "Last record"
BUTTON_HELP = "Help"
BUTTON_FEEL = "Ask me how I feel"

def get_base_reply_keyboard():
    keyboard = [
        [
            KeyboardButton(BUTTON_LAST_RECORD),
        ],
        [
            KeyboardButton(BUTTON_FEEL),
        ],
        [
            KeyboardButton(BUTTON_HELP),
        ],
    ]
    return ReplyKeyboardMarkup(
        keyboard = keyboard,
        resize_keyboard = True,
    )