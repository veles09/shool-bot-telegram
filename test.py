import requests
from datetime import datetime
import telebot
# fathomless-basin-37475
token = "5185066102:AAE-Pxf7QOcDEi4APWGyOtCBfws9YSZNT68"
def get_date():
    req = requests.get("https://yobit.net/api/3/ticker/usd_rur")
    response = req.json()
    sell_price = response["usd_rur"]["sell"]
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nsell usd - {sell_price:2g} rub")

def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start_message(message):
        bot.send_message(message.chat.id, "Привет бедотрейдер")
    
    @bot.message_handler(content_types=["text"])
    def send_text(message):
        if message.text.lower() == "price":
            try:
                req = requests.get("https://yobit.net/api/3/ticker/usd_rur")
                response = req.json()
                sell_price = response["usd_rur"]["sell"]
                bot.send_message(message.chat.id, f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nsell usd - {sell_price:2g} rub")

            except Exception as ex:
                print(ex)
                bot.send_message(message.chat.id, "wrong")
        else:
            bot.send_message(message.chat.id, "Не понял команду")
    bot.polling()



if __name__ == '__main__':
    # get_date()
    telegram_bot(token)