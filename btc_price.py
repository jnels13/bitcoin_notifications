import requests, os

#Load alphavantage key and save URL
working_dir = os.getcwd()
print(working_dir)
with open(working_dir+"/Documents/Python_Projects/Bitcoin_Notifications/bitcoin_notifications/alpha_api_key.txt", 'r') as file:
    alpha_key = file.read()
bitcoin_api_url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey="+alpha_key

response = requests.get(bitcoin_api_url)
response_json = response.json()
cur_btc_value = round(float(response_json['Realtime Currency Exchange Rate']['5. Exchange Rate']),2)

print(cur_btc_value)