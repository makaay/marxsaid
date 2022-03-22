#!/usr/bin/env python3

import json, requests 

url = requests.get("https://marxsaid.com/quote")
text = url.text
data = json.loads(text)

print(f"{data['Author']} said:")

print(f'\"{data["quote"]}\"')
