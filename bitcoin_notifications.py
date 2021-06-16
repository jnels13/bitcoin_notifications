import requests
bitcoin_api_url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo"
response = requests.get(bitcoin_api_url)
response_json = response.json()
print(response_json)
