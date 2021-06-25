# Project from https://realpython.com/python-bitcoin-ifttt/
import requests, os, time
from twilio.rest import Client
from datetime import datetime

#Load alphavantage key and save URL
with open("/Users/joenelson/Documents/Python_Projects/Bitcoin_Notifications/bitcoin_notifications/alpha_api_key.txt", 'r') as file:
    alpha_key = file.read()
bitcoin_api_url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey="+alpha_key

# Import SMS tokens/numbers
with open("/Users/joenelson/Documents/Python_Projects/Bitcoin_Notifications/bitcoin_notifications/twilio_id_token.txt", 'r') as file:
    twilio_key = file.read()
with open("/Users/joenelson/Documents/Python_Projects/Bitcoin_Notifications/bitcoin_notifications/twilio_account_sid.txt", 'r') as file:
    twilio_sid = file.read()
with open("/Users/joenelson/Documents/Python_Projects/Bitcoin_Notifications/bitcoin_notifications/my_number.txt", 'r') as file:
    my_number = file.read()


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

def send_sms(message, to_number=my_number):
    account_sid = twilio_sid
    auth_token  = twilio_key
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to=to_number, 
        from_="+12028001098",
        body=message)
    print(message.sid)

bc_price_threshold = 35500
change_threshold = 0.001
sleep_time = 10

def main(): 

    price = get_latest_bitcoin_price()
    message = "Bitcoin price is $"+str(price)
    send_sms(message)
    time.sleep(sleep_time)

    while True:
        new_price = get_latest_bitcoin_price()
        percent_change = abs((new_price-price)/price)
        if percent_change > change_threshold:
            message("Bitcoin price change of "+str(percent_change)+"%, now at $"+str(new_price))
            send_sms(message)
        time.sleep(sleep_time)

if __name__ == "__main__":
    main()