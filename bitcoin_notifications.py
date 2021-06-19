# Project from https://realpython.com/python-bitcoin-ifttt/
import requests, os

#Load key
working_dir = os.getcwd()
with open(working_dir+"/Documents/Python_Projects/Bitcoin_Notifications/bitcoin_notifications/alpha_api_key.txt", 'r') as file:
    alpha_key = file.read()

#Request exchange rate Bitcoin to US Dollars
bitcoin_api_url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey="+alpha_key
response = requests.get(bitcoin_api_url)
response_json = response.json()
cur_btc_value = response_json['Realtime Currency Exchange Rate']['5. Exchange Rate']



