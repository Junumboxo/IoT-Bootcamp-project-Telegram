from msg_buttons import TITLES_FEEL

msg_start = "Hello! \nI am your climate control bot. I can provide information about the clime in your home. I will also sometimes ask how you feel. For more info enter command /help"
msg_help = "This is help."
msg_echo = "Sorry. I don't understand you."
msg_feel = "How do you feel? Haven't you got any difficulties of breath?"
msg_feel_GOOD = "You have chosen {}.\nGlad you're OK!".format(TITLES_FEEL['INLINE_BUTTON_GOOD'])
msg_feel_BAD = "You have chosen {}.\nOh, I'm sorry 😥\nGo have some tea".format(TITLES_FEEL['INLINE_BUTTON_BAD'])
msg_feel_SEND = "Sending your reply to the server..."
msg_feel_DISCARD = "OK, tell me one more time how you feel"