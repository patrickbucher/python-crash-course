class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'{self.restaurant_name} is a restaurant with '
              f'{self.cuisine_type} cuisine')

    def open_restaurant(self):
        print(f'the Restaurant {self.restaurant_name} is open')


bahnhoefli = Restaurant('Bahnhöfli', 'inferior')
bahnhoefli.describe_restaurant()
bahnhoefli.open_restaurant()

sternen = Restaurant('Sternen', 'traditional Swiss')
sternen.describe_restaurant()

mailing = Restaurant('Mai Ling', 'Chinese')
mailing.describe_restaurant()
