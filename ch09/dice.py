from random import randint


class Die:

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)


die = Die()
for i in range(0, 10):
    print(die.roll_die())
