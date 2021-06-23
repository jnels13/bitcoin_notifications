
import requests, os

# Pull the Zapier key
working_dir = os.getcwd()
payload = {
            "contact": 
                {"name":"joe",
                 "phone":"123-456-7890",
                 "address":"who cares"},
            "information":
                {"date":"12-23-45",
                 "time":"23:12",
                 "subject":"no subject"}
          }
with open(working_dir+"/Documents/Python_Projects/Bitcoin_Notifications/bitcoin_notifications/zapier_key_url.txt", 'r') as file:
    zap_key = file.read()

    # Request webhook previously set up on Zapier
zap_webhook_url = zap_key

test_webhook = "https://webhook.site/dd566286-7ea1-4caf-bb7f-3b97d3f25b3b"
requests.post(test_webhook, data=payload)