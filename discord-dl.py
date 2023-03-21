#!/bin/python3

# This script downloads the message history of a Discord channel using HTTP GET
# requests.

import requests
import json

f = open('config.json', 'r')
config = json.load(f)
f.close()

url = 'https://discord.com/api/v9/channels/' + config['id'] + '/messages'
headers = {
    'Authorization': config['token'] 
    }

response = requests.get(url, headers=headers)
url += '?before='

while True:
    if response.status_code != 200:
        print(response.status_code)
        print(response.reason)
        break

    messages = response.json()
    for message in messages:
        if message['content'] == '':
            continue
        print(name + message['content'])

    response = requests.get(url + messages[-1]['id'], headers=headers)
