from telegram import InlineKeyboardButton, InlineKeyboardMarkup

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