guests = ['George Carlin', 'Thomas Bernhard', 'Pieter Hintjens']
print(guests[0], 'will rant about the United States')
print(guests[1], 'will rant about Austria and the rest of Europe')
print(guests[2], 'will rant about Software')

print('Unfortunately,', guests.pop(0), 'cannot make it')
guests.insert(0, 'Henry L. Mencken')

print(guests[0], 'will rant about the United States')
print(guests[1], 'will rant about Austria and the rest of Europe')
print(guests[2], 'will rant about Software')

print('Now that I found a bigger table, let us invite some more people')
guests.insert(0, 'George W. Bush')
guests.insert(2, 'Bruno Kreisky')
guests.append('Bill Gates')

print(guests[0], 'will lie about the war in Iraq')
print(guests[1], 'will rant about the United States')
print(guests[2], 'will talk about Austria')
print(guests[3], 'will rant about Austria')
print(guests[4], 'will rant about Software')
print(guests[5], 'will brag about Microsoft')

print('Unfortunately, I have only enough money to invite two guests')
print(f'Sorry, {guests.pop()}, not enough money for you')
print(f'Sorry, {guests.pop()}, you cannot come')
print(f'Sorry, {guests.pop()}, I am short of money')
print(f'Sorry, {guests.pop()}, I do not like bores')

print(guests[0], 'can still come')
print(guests[1], 'is still invited, too')

del guests[1]
del guests[0]

print(guests)
