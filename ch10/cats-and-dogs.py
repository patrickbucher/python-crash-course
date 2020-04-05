def output(filename):
    try:
        with open(filename) as f:
            print(f.read())
    except FileNotFoundError:
        print(f'unable to read {filename}')


output('cats.txt')
output('dogs.txt')
