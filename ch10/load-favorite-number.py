import json

try:
    with open('favorite-number.json') as f:
        number = json.load(f)
        print(f'I know your favorite number! It is {number}.')
except FileNotFoundError:
    pass
