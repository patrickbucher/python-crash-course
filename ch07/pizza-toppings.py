prompt = 'Which topping would you like to add to your pizza?'
prompt += '\nType "quit" when you are finished. '
topping = ''
active = True
while active:
    topping = input(prompt)
    if topping == 'quit':
        active = False
    else:
        print(f'I will add {topping} to your pizza.')
