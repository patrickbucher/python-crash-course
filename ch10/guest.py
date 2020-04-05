username = input('What is your name, please? ')
with open('guest.txt', 'w') as f:
    f.write(username)
