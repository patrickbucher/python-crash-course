with open('learning_python.txt') as f:
    content = f.read()
print(content.rstrip())

with open('learning_python.txt') as f:
    for line in f:
        print(line.rstrip())

with open('learning_python.txt') as f:
    lines = f.readlines()
for line in lines:
    print(line.rstrip())
