def output(filename):
    try:
        with open(filename) as f:
            print(f.read())
    except FileNotFoundError:
        pass


output('cats.txt')
output('dogs.txt')
