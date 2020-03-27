rivers = {
    'nile': 'egypt',
    'yangtse': 'china',
    'amazonas': 'brasil',
    'mississippi': 'usa',
    'don': 'russia',
}

for river, country in rivers.items():
    print(f'The {river.title()} runs through {country.title()}')
