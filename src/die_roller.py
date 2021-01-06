import random


class DieRoller:
    def __init__(self):
        pass

    def d6(self):
        return random.randint(1, 6)

    def d10(self):
        return random.randint(1, 10)

    def d20(self):
        return random.randint(1, 20)

    def d100(self):
        return random.randint(1, 100)
