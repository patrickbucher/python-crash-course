def create_sandwich(*ingredients):
    print('You ordered a sandwich that contains:')
    for ingredient in ingredients:
        print(f'- {ingredient}')
    print()


create_sandwich('Mozzarella', 'Tomato', 'Butter')
create_sandwich('Salami', 'Cheddar', 'Butter')
create_sandwich('Cheese')
