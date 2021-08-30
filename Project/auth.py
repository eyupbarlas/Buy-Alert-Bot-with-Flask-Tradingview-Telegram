import hashlib

#! Tradingview Webhook Token 
pin = '1234'
#* Generating an unique key. Extra secure
def get_token():
    token = hashlib.sha224(pin.encode('utf-8'))
    return token.hexdigest()
