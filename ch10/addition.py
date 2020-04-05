a = input('First Number:  ').strip()
b = input('Second Number: ').strip()
try:
    c = int(a) + int(b)
    print(f'{a} + {b} = {c}')
except ValueError:
    print('You entered an invalid number.')
