import requests
import json


response = requests.get("https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow")

for item in response.json()['items']:
    print(item['title'])
    print(item['link'])
    print()