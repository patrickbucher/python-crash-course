from user import User

alice = User('Alice', 'Bobsky', 1000, 'USA')
mallory = User('Mallory', 'Malice', 1001, 'France')
zak = User('Zacharias', 'Finkelstein', 1002, 'Israel')

alice.describe_user()
mallory.describe_user()
zak.describe_user()

alice.greet_user()
mallory.greet_user()
zak.greet_user()
