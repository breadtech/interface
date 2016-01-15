import json

fp = open('menu.json')
s = fp.read()
# implement security here
# - bad to just pass in a string from a config file
menu = json.loads(s)
