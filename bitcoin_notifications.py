# Project from https://realpython.com/python-bitcoin-ifttt/
import requests, os, time
from datetime import datetime

# Pull the IFTTT key and insert into URL
with open("/Users/joenelson/Documents/Python_Projects/Bitcoin_Notifications/bitcoin_notifications/ifttt_key.txt", 'r') as file:
    ifttt_key = file.read()
ifttt_webhook_url = "https://maker.ifttt.com/trigger/{}/with/key/"+ifttt_key
print(ifttt_webhook_url)
#Load alphavantage key and save URL
with open("/Users/joenelson/Documents/Python_Projects/Bitcoin_Notifications/bitcoin_notifications/alpha_api_key.txt", 'r') as file:
    alpha_key = file.read()
bitcoin_api_url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey="+alpha_key


def get_latest_bitcoin_price():
    """
    Requests latest bitcoin-USD exchange rate from
    alphavantage.com.  No arguments, returns a 2-
    decimal place float.
    """

    response = requests.get(bitcoin_api_url)
    response_json = response.json()
    cur_btc_value = float(response_json['Realtime Currency Exchange Rate']['5. Exchange Rate'])
    return(round(cur_btc_value, 2))

def post_webhook (event, value):
    payload = {"Value1": value}
    #inserts desired event
    ifttt_event_url = ifttt_webhook_url.format(event)
    #send http post to webhook URL
    requests.post(ifttt_event_url, data=payload)
    print(payload)

bc_price_threshold = 10000

def main(): 

    while True:
        price = get_latest_bitcoin_price()
        print(price)

        if float(price) > bc_price_threshold:
            post_webhook('bitcoin_price', price)

        time.sleep(30)

if __name__ == "__main__":
    main()