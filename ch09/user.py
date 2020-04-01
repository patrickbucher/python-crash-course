class User:

    def __init__(self, first_name, last_name, user_id, country):
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.country = country
        self.login_attempts = 0

    def describe_user(self):
        print(f'{self.first_name} {self.last_name} [uid: {self.user_id}] '
              f'is from {self.country}')

    def greet_user(self):
        print(f'Hello, {self.first_name} {self.last_name}!')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
