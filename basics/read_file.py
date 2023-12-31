import json

with open('fake_fruit.json', 'r') as f:
    data = json.load(f)

print(data)


