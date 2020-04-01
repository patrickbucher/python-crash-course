from user import User


class Admin(User):

    def __init__(self, first_name, last_name, user_id, country, privileges):
        super().__init__(first_name, last_name, user_id, country)
        self.privileges = privileges

    def show_privileges(self):
        print('Bitch, I am an admin. I can do the following:')
        self.privileges.list_privileges()


class Privileges:

    def __init__(self, privileges):
        self.privileges = privileges

    def list_privileges(self):
        for privilege in self.privileges:
            print(f'- {privilege}')
        print()
