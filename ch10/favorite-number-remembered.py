import json


def save_favorite_number(filename):
    number = None
    while not number:
        try:
            number = int(input('What is your favorite number? '))
        except ValueError:
            pass

    with open(filename, 'w') as f:
        json.dump(number, f)


def load_favorite_number(filename):
    try:
        with open(filename) as f:
            number = json.load(f)
            return number
    except FileNotFoundError:
        return None


filename = 'favorite-number.json'
favorite_number = load_favorite_number(filename)
if not favorite_number:
    save_favorite_number(filename)
    favorite_number = load_favorite_number(filename)
print(f'I know your favorite number! It is {favorite_number}.')
