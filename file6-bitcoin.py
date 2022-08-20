import requests

# Add key in the key parameter in url before running the script

bitcoin_api_url = 'https://api.nomics.com/v1/currencies/ticker?key=&ids=ETH&interval=1d,30d&platform-currency=ETH&per-page=100&page=1"'
response = requests.get(bitcoin_api_url)
reponse_json = response.json()  
type(reponse_json)
print(" PRICE",reponse_json[0]['price'],"TIME-STAMP ",reponse_json[0]['price_timestamp'])

