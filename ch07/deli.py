sandwich_orders = ['thuna', 'salami', 'cheese', 'bologna']
finished_sandwiches = []

while sandwich_orders:
    order = sandwich_orders.pop(0)
    print(f'I made your {order} sandwich.')
    finished_sandwiches.append(order)

print('I made the following sandwiches:', finished_sandwiches)
