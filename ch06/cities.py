cities = {
    'Moscow': {
        'Country': 'Russia',
        'Population': 11_900_000,
        'Fact': 'You can get a haircut and buy flowers at 4 a.m.',
    },
    'London': {
        'Country': 'England',
        'Population': 8_900_000,
        'Fact': 'Has a lot of Premier League clubs.',
    },
    'New York': {
        'Country': 'USA',
        'Population': 8_300_000,
        'Fact': 'Was once called «New Amsterdam».',
    },
}

for city, facts in cities.items():
    print(city)
    for key, value in facts.items():
        print(f'\t{key}: {value}')
    print()
