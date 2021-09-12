from auth import *
from script import *
from flask import Flask, render_template, request
import json

#! Flask app init
app = Flask(__name__)

#! Index page
@app.route("/")
def index():
    return render_template('index.html', SYMBOL=SYMBOL)

#! Webhook page
@app.route("/webhook", methods=['GET', 'POST'])
def webhook():
    if request.method == "POST":
        data = json.loads(request.data)

        #* Token confirmation
        if data['token'] != get_token():
            return {
                "code": "error",
                "message": "Invalid token"
            }

        #* This is the indicator alert. 
        #* Indicator(open source library in Tradingview) used in this project is: "CM_MacD_Ult_MTF" from ChrisMoody. 
        if data['cross_histogram'] > 0:
            print("**BUY BUY BUY!**")
            telegram_bot_sendtext("***BUY BUY BUY!*** \n"+"`Symbol: {} Price: {}`".format(SYMBOL, data['bar']['open']))
            return{
                "code" : "success",
                "message" : "buy notification has been sent"
            }
        
        else:
            print("***SELL SELL SELL!***")
            telegram_bot_sendtext("***SELL SELL SELL!*** \n"+"`Symbol: {} Price: {}`".format(SYMBOL, data['bar']['open']))
            return{
                "code" : "success",
                "message" : "sell notification has been sent"
            }

    return "**Webhook Get**"


#! Flask run
if __name__ == '__main__':
    app.run(debug=True)
