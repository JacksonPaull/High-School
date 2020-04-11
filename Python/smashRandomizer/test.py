import json

with open('settings.json') as f:
    settings = json.load(f)

for f in settings:
    print(f,settings[f])
