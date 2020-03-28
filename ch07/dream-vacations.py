destinations = {}

polling = True
while polling:
    name = input('What is your name ("quit" to exit)? ')
    if name == 'quit':
        polling = False
    else:
        destination = input('Where would you like to travel? ')
        destinations[name] = destination

for name, destination in destinations.items():
    print(f'{name} would like to travel to {destination}.')
