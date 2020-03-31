class Privileges:

    def __init__(self, privileges):
        self.privileges = privileges

    def list_privileges(self):
        for privilege in self.privileges:
            print(f'- {privilege}')
        print()
