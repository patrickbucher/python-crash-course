r_emelo = {
    'first_name': 'Randy',
    'last_name': 'Emelo',
    'age': 53,
    'city': 'Fraudsterville',
}

eschuja = {
    'first_name': 'Elisabeth',
    'last_name': 'Schulze-Jägle',
    'age': 49,
    'city': 'Schwäbisch Gmünd',
}

dirty_harry = {
    'first_name': 'Harald',
    'last_name': 'Burger',
    'age': 51,
    'city': 'Javaland',
}

people = [r_emelo, eschuja, dirty_harry]

for person in people:
    print(f"His/her name is {person['first_name']} {person['last_name']}.")
    print(f"He/she is {person['age']} years old, lives in {person['city']}.\n")
