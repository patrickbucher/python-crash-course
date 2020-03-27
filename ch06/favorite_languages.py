favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

people = [
    'jen',
    'edward',
    'tom',
    'phil',
    'george',
]

for person in people:
    if person in favorite_languages.keys():
        print(f'Thanks, {person}, for responding to our poll!')
    else:
        print(f'Please, {person}, take our poll on programming languages!')
