langs = ['C', 'C++', 'Python', 'C#', 'Rust', 'Go', 'JavaScript', 'awk']

langs.append('Ruby')
ruby = langs.pop()

del langs[1]
langs.remove('C#')
langs.insert(0, 'Assembly')

print(f'{len(langs)} programming languages')
langs.sort(reverse=True)
print(langs)

print(sorted(langs))
langs.reverse()
print(langs)
