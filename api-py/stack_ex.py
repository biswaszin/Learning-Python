import requests
import json

"""
    Requests is a HTTP library for Python
    json. as you can imagine. json.
"""

response = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')
data_raw = response.json()
print(response)

for data in data_raw['items']:
    print(data['title'])
