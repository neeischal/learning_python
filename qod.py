# Quote of the Day program 
import requests

URL = "https://quotes.rest/quote/random"
response = requests.get(url=URL)

json = response.json()
print(json['contents']['quotes'][0]['quote'])