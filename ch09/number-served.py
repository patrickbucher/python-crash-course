class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f'{self.restaurant_name} is a restaurant with '
              f'{self.cuisine_type} cuisine')

    def open_restaurant(self):
        print(f'the Restaurant {self.restaurant_name} is open')

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self):
        self.number_served += 1


bahnhoefli = Restaurant('Bahnhöfli', 'inferior')
bahnhoefli.describe_restaurant()
bahnhoefli.open_restaurant()

sternen = Restaurant('Sternen', 'traditional Swiss')
sternen.describe_restaurant()

mailing = Restaurant('Mai Ling', 'Chinese')
mailing.describe_restaurant()
mailing.number_served = 10
print(mailing.number_served)
mailing.set_number_served(20)
mailing.increment_number_served()
print(mailing.number_served)
