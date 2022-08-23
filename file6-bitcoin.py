# import requests

# # Add key in the key parameter in url before running the script, remove curly brackets

# eth_api_url = 'https://api.nomics.com/v1/currencies/ticker?key={your_key}&ids=ETH&interval=1d,30d&platform-currency=ETH&per-page=100&page=1'
# response = requests.get(eth_api_url)
# response_json = response.json()  
# type(response_json)
# print(" PRICE",response_json[0]['price'],"TIME-STAMP ",response_json[0]['price_timestamp'])

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

# ifttt_webhook_url = 'https://maker.ifttt.com/trigger/test_event/json/with/key/{your_key}'
# requests.post(ifttt_webhook_url)

# setting up emergency alerts
# finalizing the code

import requests
import time
from datetime import datetime

ETH_API_URL = 'https://api.nomics.com/v1/currencies/ticker?key={your_key}&ids=ETH&interval=1d,30d&platform-currency=ETH&per-page=100&page=1'
IFTTT_WEBHOOKS_URL = 'https://maker.ifttt.com/trigger/{}/with/key/{your_key}'

# you can set currency etherium, bitcoin, dogecoin, etc, depends upon you.

def get_latest_eth_price():
    response = requests.get(ETH_API_URL)
    response_json = response.json()
    return float(response_json[0]['price'])  

def post_ifttt_webhook(event, value):
    data = {'value1': value}  
    ifttt_event_url = IFTTT_WEBHOOKS_URL.format(event)  # Inserts our desired event
    print(event, value, 'checking event and value')
    requests.post(ifttt_event_url, json=data)  # Sends a HTTP POST request to the webhook URL

def format_eth_history(eth_history):
    rows = []
    for eth_price in eth_history:
        date = eth_price['date'].strftime('%d.%m.%Y %H:%M')  
        price = eth_price['price']
        row = '{}: $<b>{}</b>'.format(date, price)
        rows.append(row)

    # Use a <br> (break) tag to create a new line
    return '<br>'.join(rows)  

def main():
    eth_history = []
    ETH_PRICE_THRESHOLD = 2000
    while True:
        price = get_latest_eth_price()
        date = datetime.now()
        eth_history.append({'date': date, 'price': price})

        # Send an emergency notification
        if price < ETH_PRICE_THRESHOLD:
            post_ifttt_webhook('eth_price_emergency', price)

        # Send a Telegram notification
        if len(eth_history) == 5:  # Once we have 5 items in our etherium_history send an update
            post_ifttt_webhook('eth_price_update', format_eth_history(eth_history))
            # Reset the history
            eth_history = []

        time.sleep(5*60)  # Sleep for n-minutes (for testing purposes you can set it to whatever you want)

if __name__ == '__main__':
    main()