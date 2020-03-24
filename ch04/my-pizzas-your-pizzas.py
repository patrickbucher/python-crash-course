pizzas = ['Margherita', 'Prosciutto', 'Calzone']

friend_pizzas = pizzas[:]
pizzas.append('Hawaii')

for pizza in pizzas:
    print(f'My favorite pizzas are: {pizza}')

for pizza in friend_pizzas:
    print(f'My friend\'s favorite pizzas are: {pizza}')
