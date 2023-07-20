import random


class User:
    def __init__(self, username: str, email: str, department_id: int):
        self.username = username
        self.email = email
        self.id = random.randint(1, 1000)
        self.departmentId = department_id
