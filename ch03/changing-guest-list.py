guests = ['George Carlin', 'Thomas Bernhard', 'Pieter Hintjens']
print(guests[0], 'will rant about the United States')
print(guests[1], 'will rant about Austria and the rest of Europe')
print(guests[2], 'will rant about Software')

print('Unfortunately,', guests.pop(0), 'cannot make it')
guests.insert(0, 'Henry L. Mencken')

print(guests[0], 'will rant about the United States')
print(guests[1], 'will rant about Austria and the rest of Europe')
print(guests[2], 'will rant about Software')
