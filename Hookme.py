
import requests, os

# Pull the Zapier key
working_dir = os.getcwd()
with open(working_dir+"/Documents/Python_Projects/Bitcoin_Notifications/bitcoin_notifications/zapier_key_url.txt", 'r') as file:
    zap_key = file.read()

    # Request webhook previously set up on Zapier
zap_webhook_url = zap_key
requests.post(zap_webhook_url)