
import requests, os

# Pull the IFTTT key
working_dir = os.getcwd()
with open(working_dir+"/Documents/Python_Projects/Bitcoin_Notifications/bitcoin_notifications/ifttt_key.txt", 'r') as file:
    ifttt_key = file.read()

# Request webhook previously set up on IFTTT
ifttt_webhook_url = "https://maker.ifttt.com/trigger/{}/with/key/"+ifttt_key
#requests.post(zap_webhook_url)


payload = {"name":"joe"}

# with open(working_dir+"/Documents/Python_Projects/Bitcoin_Notifications/bitcoin_notifications/zapier_key_url.txt", 'r') as file:
#     zap_key = file.read()

event = "test_event"
ifttt_event_url = ifttt_webhook_url.format(event)

# test_webhook = "https://webhook.site/dd566286-7ea1-4caf-bb7f-3b97d3f25b3b"
requests.post(ifttt_event_url, data=payload)