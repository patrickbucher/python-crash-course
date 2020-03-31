class User:

    def __init__(self, first_name, last_name, user_id, country):
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.country = country

    def describe_user(self):
        print(f'{self.first_name} {self.last_name} [uid: {self.user_id}] '
              f'is from {self.country}')

    def greet_user(self):
        print(f'Hello, {self.first_name} {self.last_name}!')


alice = User('Alice', 'Bobsky', 1000, 'USA')
mallory = User('Mallory', 'Malice', 1001, 'France')
zak = User('Zacharias', 'Finkelstein', 1002, 'Israel')

alice.describe_user()
mallory.describe_user()
zak.describe_user()

alice.greet_user()
mallory.greet_user()
zak.greet_user()