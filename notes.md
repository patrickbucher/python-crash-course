# String Methods

- rstrip()
- lstrip()
- strip()

- upper()
- lower()
- title()

# Lists

- list.append(item)
- item = items.pop()
- item = items.pop(index)
- del items[index]
- items.remove(item)
- insert(index, item)
- len(items)
- items = list(range(0, 10))

## Order

- list.sort()
- list.sort(reverse=True)
- list = sorted(list)
- list = sorted(list, reverse=True)
- list.reverse()

## Range

- range(5): 0..4
- range(1, 5): 1..4
- range(1, 10, 3): 1, 4, 7

## Statistics

- min(items)
- max(items)
- sum(items)

## Slicing

- copy = items[:]

# Dictionaries

- items = {}
- item = items.get(key, default)

## Looping Over Keys and Values

for key in dictionary: # implicit
    print(key, dictionary[key])
    
for key in dictionary.keys(): # explicit
    print(key, dictionary[key])

for value in dictionary.values():
    print(value)

for key, value in dictionary.items():
    print(key, value)

# Sets

- set(items)
- uniqueitems = {'foo', 'bar', 'baz'}

# Input

- string = input("prompt")

# Casting

- number = int(string)

# Standard Library

## random

- random.randint(from, to)
- random.choice(['foo', 'bar'])
