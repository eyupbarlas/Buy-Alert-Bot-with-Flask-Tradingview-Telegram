# Buy Alert Bot by Bzzman

## About Project
  ***Work in progress.*** This bot sends notifications to your Telegram to buy the coins you want. You need a Tradingview account to handle the webhooks. You can pick any indicator and change the settings as you wish. I chose an open source indicator("StochasticRSI & RSI & MACD") from Crypto_Adhyeta. This bot detects the alert, sends you "Buy" notifications via Telegram. This project is a simple version of my [latest project](https://github.com/eyupbarlas/Crypto-Trading-Bot-with-Tradingview-Binance-Heroku-and-Telegram). Feel free the check out!
  
## Features
* Real time data from Tradingview using webhooks
* Telegram notifications when a buy alert raises.
* User interface ***on progress***.

## How To Use
### Required Libs
* [Flask Framework](https://flask.palletsprojects.com/en/2.0.x/ "Python Flask")
```
pip install Flask
```
### Deploying Python Flask App to Heroku
> [Useful documentation by Heroku](https://devcenter.heroku.com/articles/getting-started-with-python "python app deployment")
#### Useful terminal commands after deployment:
* After making a change on production: `git add .` + `git commit -am "your message"`
* Pushing the app to the cloud: `git push heroku master`

### Setting Up Telegram Bot
To build a bot for Telegram, you need to talk to [BotFather](https://telegram.me/botfather "BotFather") and follow the simple steps. He will give you a token to start a chat with your bot. 

### Setting Up the Tradingview Webhook
![webhook](https://user-images.githubusercontent.com/72407947/131344141-d93e9c13-dcd3-4a4b-84c4-5d207deae9ec.jpg)

For the message section, enter the message in this repository.


> **Personal Information**
> 
>> Eyüp Barlas  eyupbarlas2134@gmail.com
>> For more projects, [click here](https://github.com/eyupbarlas "my repos").
