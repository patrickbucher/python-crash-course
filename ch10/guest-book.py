with open('guest_book.txt', 'w') as f:
    while True:
        name = input('What is your name, please? ').rstrip()
        if name:
            f.write(f'{name}\n')
        else:
            break
