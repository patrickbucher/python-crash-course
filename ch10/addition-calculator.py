def input_number(prompt):
    x = ''
    while x == '':
        number = input(prompt).strip()
        try:
            x = int(number)
        except ValueError:
            print(f'You entered an invalid number "{number}".')
    return x


a = input_number('first number:  ')
b = input_number('second number: ')
c = a + b
print(f'{a}+{b}={c}')
