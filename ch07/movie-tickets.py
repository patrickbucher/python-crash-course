prompt = 'How old are you? '
prompt += '\nType "quit" when you are finished. '

prompt = ''
while prompt != 'quit':
    age = int(input(prompt).strip())
    if age < 3:
        print('Your ticket is free')
    elif age >= 3 and age <= 12:
        print('Your ticket is $10')
    elif age > 12:
        print('Your ticket is $15')
