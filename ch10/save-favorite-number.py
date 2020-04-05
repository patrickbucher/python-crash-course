import json

number = None
while not number:
    try:
        number = int(input('What is your favorite number? '))
    except ValueError:
        pass

with open('favorite-number.json', 'w') as f:
    json.dump(number, f)
