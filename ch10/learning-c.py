with open('learning_python.txt') as f:
    for line in f:
        line = line.rstrip().replace('Python', 'Nim')
        print(line)
