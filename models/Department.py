import random


class Department:
    def __init__(self, name):
        self.name = name
        self.id = random.randint(1, 1000)

    def __repr__(self):
        return str({"id": self.id, "name": self.name})
