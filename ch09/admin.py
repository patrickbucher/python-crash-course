from privileges import Privileges
from users import User


class Admin(User):

    def __init__(self, first_name, last_name, user_id, country, privileges):
        super().__init__(first_name, last_name, user_id, country)
        self.privileges = privileges

    def show_privileges(self):
        print('Bitch, I am an admin. I can do the following:')
        self.privileges.list_privileges()


root = Admin('Ruth', 'Rutherford', 1, 'Switzerland', Privileges(
    ['spy on you', 'delete your files', 'read your email']))
root.show_privileges()
