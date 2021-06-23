# Project from https://realpython.com/python-bitcoin-ifttt/
import requests, os

# Pull the Zapier key
working_dir = os.getcwd()
with open(working_dir+"/Documents/Python_Projects/Bitcoin_Notifications/bitcoin_notifications/zapier_key_url.txt", 'r') as file:
    zap_key = file.read()

# Request webhook previously set up on Zapier
zap_webhook_url = zap_key
#requests.post(zap_webhook_url)

#Load alphavantage key and save URL
working_dir = os.getcwd()
with open(working_dir+"/Documents/Python_Projects/Bitcoin_Notifications/bitcoin_notifications/alpha_api_key.txt", 'r') as file:
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
    # payload sent to Zapier
    data = {"value1": value}
    #inserts desired event
    zap_event_url = zap_webhook_url + "/" + event

# Request webhook previously set up on Zapier
zap_webhook_url = zap_key
requests.post(zap_webhook_url)


def __main__(): 
    pass

if __name__ == "__main__":
    main()



