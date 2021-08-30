import hashlib

#! Tradingview Webhook Token 
# 99fb2f48c6af4761f904fc85f95eb56190e5d40b1f44ec3a9c1fa319 
pin = '1234'
#* Generating an unique key. Extra secure
def get_token():
    token = hashlib.sha224(pin.encode('utf-8'))
    return token.hexdigest()
