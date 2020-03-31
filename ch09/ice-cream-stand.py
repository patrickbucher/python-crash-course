from restaurant import Restaurant


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        if self.flavors:
            print('We offer the following flavors:')
            for flavor in self.flavors:
                print(f'- {flavor}')
            print()


gelato_schettino = IceCreamStand(
    'Gelato Schettino',
    'Ice Cream',
    ['Chocolate',
     'Vanilla',
     'Strawberry'])

gelato_schettino.describe_restaurant()
gelato_schettino.open_restaurant()
gelato_schettino.display_flavors()
