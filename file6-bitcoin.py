import requests

# Add key in the key parameter in url before running the script, remove curly brackets

bitcoin_api_url = 'https://api.nomics.com/v1/currencies/ticker?key={your_key}&ids=ETH&interval=1d,30d&platform-currency=ETH&per-page=100&page=1'
response = requests.get(bitcoin_api_url)
reponse_json = response.json()  
type(reponse_json)
print(" PRICE",reponse_json[0]['price'],"TIME-STAMP ",reponse_json[0]['price_timestamp'])

# After installing IFTT on your phone, setup your applet for notification purpose with following steps:
# 1.Click on the big “this” button
# 2.Search for the “webhooks” service and select the “Receive a web request” trigger
# 3.Let’s name the event test_event
# 4.Now select the big “that” button
# 5.Search for the “notifications” service and select the “Send a notification from the IFTTT app”
# 6.Change the message to I just triggered my first IFTTT action! and click on “Create action”
# 7.Click on the “Finish” button and we’re done 
# After this, open documentation of IFTTT webhook and your webhook URL will appear their with the event name you set and your key.
# Following code will send an HTTP POST request to the IFTTT webhook URL using the requests.post() function and you will get notification on your phone.

# Make sure that your key is in the URL
# Add key in the key parameter in url before running the script, remove curly brackets

ifttt_webhook_url = 'https://maker.ifttt.com/trigger/test_event/json/with/key/{your_key}'
requests.post(ifttt_webhook_url)

# setting up emergency alerts

