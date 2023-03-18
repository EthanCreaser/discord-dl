#!/bin/python3

import requests
import json

# Load sensitive information from a .json configuration file
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
    # Gaurd clause for bad HTTP status code
    if response.status_code != 200:
        print(response.status_code)
        print(response.reason)
        break

    messages = response.json()
    for message in messages:
        if message['content'] == '':
            continue
        if message['author']['username'] == 'Severian':
            name = 'Ethan: '
        else:
            name = 'Tori:  '
        print(name + message['content'])

    response = requests.get(url + messages[-1]['id'], headers=headers)
