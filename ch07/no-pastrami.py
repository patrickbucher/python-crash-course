sandwich_orders = [
    'thuna',
    'pastrami',
    'salami',
    'pastrami',
    'cheese',
    'pastrami',
    'bologna'
]
finished_sandwiches = []

print('We have run out of pastrami.')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    order = sandwich_orders.pop(0)
    print(f'I made your {order} sandwich.')
    finished_sandwiches.append(order)

print('I made the following sandwiches:', finished_sandwiches)
