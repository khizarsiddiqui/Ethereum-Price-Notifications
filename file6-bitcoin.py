# import requests

# # Add key in the key parameter in url before running the script, remove curly brackets

# bitcoin_api_url = 'https://api.nomics.com/v1/currencies/ticker?key={your_key}&ids=ETH&interval=1d,30d&platform-currency=ETH&per-page=100&page=1'
# 
# response = requests.get(bitcoin_api_url)
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
# 
# requests.post(ifttt_webhook_url)

# setting up emergency alerts
# finalizing the code

import requests
import time
from datetime import datetime

BITCOIN_PRICE_THRESHOLD = 10000
BITCOIN_API_URL = 'https://api.nomics.com/v1/currencies/ticker?key={your_key}&ids=ETH&interval=1d,30d&platform-currency=ETH&per-page=100&page=1'
IFTTT_WEBHOOKS_URL = 'https://maker.ifttt.com/trigger/test_event/json/with/key/{your_key}'

def get_latest_bitcoin_price():
    response = requests.get(BITCOIN_API_URL)
    response_json = response.json()
    return float(response_json[0]['price'])  

def post_ifttt_webhook(event, value):
    data = {'value1': value}  # The payload that will be sent to IFTTT service
    ifttt_event_url = IFTTT_WEBHOOKS_URL.format(event)  # Inserts our desired event
    requests.post(ifttt_event_url, json=data)  # Sends a HTTP POST request to the webhook URL

def format_bitcoin_history(bitcoin_history):
    rows = []
    for bitcoin_price in bitcoin_history:
        date = bitcoin_price['date'].strftime('%d.%m.%Y %H:%M')  # Formats the date into a string: '24.02.2018 15:09'
        price = bitcoin_price['price']
        # <b> (bold) tag creates bolded text
        row = '{}: $<b>{}</b>'.format(date, price)  # 24.02.2018 15:09: $<b>10123.4</b>
        rows.append(row)

    # Use a <br> (break) tag to create a new line
    return '<br>'.join(rows)  # Join the rows delimited by <br> tag: row1<br>row2<br>row3

def main():
    bitcoin_history = []
    while True:
        price = get_latest_bitcoin_price()
        date = datetime.now()
        bitcoin_history.append({'date': date, 'price': price})

        # Send an emergency notification
        if price < BITCOIN_PRICE_THRESHOLD:
            post_ifttt_webhook('bitcoin_price_emergency', price)

        # Send a Telegram notification
        if len(bitcoin_history) == 5:  # Once we have 5 items in our bitcoin_history send an update
            post_ifttt_webhook('bitcoin_price_update', format_bitcoin_history(bitcoin_history))
            # Reset the history
            bitcoin_history = []

        time.sleep(5 * 60)  # Sleep for 5 minutes (for testing purposes you can set it to a lower number)

if __name__ == '__main__':
    main()