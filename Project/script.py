import requests
from config import *


"""
          .-.         .--''-.
        .'   '.     /'       `.
        '.     '. ,'          |
     o    '.o   ,'        _.-'
      \.--./'. /.:. :._:.'
     .'    '._-': ': ': ': ':
    :(#) (#) :  ': ': ': ': ':>-
     ' ____ .'_.:' :' :' :' :'
      '\__/'/ | | :' :' :'
            \  \ \
            '  ' '      The Bzzman.
"""
 
#! Global variables 
SYMBOL = 'SOLBUSD'

#! Telegram Notification
def telegram_bot_sendtext(bot_message):
    bot_token = BOT_TOKEN
    bot_chatID = BOT_CHATID
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + \
                '&parse_mode=Markdown&text=' + bot_message

    requests.get(send_text)
