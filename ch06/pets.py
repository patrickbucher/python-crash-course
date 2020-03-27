ms_meow = {
    'kind': 'Cat',
    'owner': 'Catherine C. Owner',
}

mr_doggy = {
    'kind': 'Dog',
    'owner': 'Crazy Bitch',
}

randy_the_rat = {
    'kind': 'Rat',
    'owner': 'Some Punk',
}

pets = [ms_meow, mr_doggy, randy_the_rat]

for pet in pets:
    print(f"A {pet['kind']} owned by {pet['owner']}")
