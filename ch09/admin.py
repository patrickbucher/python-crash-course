from acl import Admin, Privileges
from users import User


root = Admin('Ruth', 'Rutherford', 1, 'Switzerland', Privileges(
    ['spy on you', 'delete your files', 'read your email']))
root.show_privileges()
