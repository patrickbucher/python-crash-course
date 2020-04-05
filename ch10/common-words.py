with open('wilde_de-profundis.txt') as f:
    words = f.read().lower().split()
n = words.count('the')
print(f'the word "the" appears {n} times in the text')
