from typing import List
from dao.Department import DepartmentDAO
from models.User import User


class UserDAO:
    def __init__(self, department_dao: DepartmentDAO):
        self.users: List[User] = []
        self.department_dao = department_dao

    def get_all_users(self):
        users_with_department = []
        for user in self.users:
            department = self.department_dao.get_single_department(user.departmentId)
            users_with_department.append(
                {"id": user.id, "username": user.username, "email": user.email, "department": department})
        return users_with_department

    def get_single_user(self, _id: int):
        for user in self.users:
            if user.id == _id:
                department = self.department_dao.get_single_department(user.departmentId)
                return {"id": user.id, "username": user.username, "email": user.email, "department": department}

        raise Exception(f"User with id of {_id} does not exist")

    def add_user(self, username: str, email: str, department_id: int):
        if not self.department_exist(department_id):
            raise Exception(
                f"Department with id of {department_id} does not exist. You cannot associate a user with a department "
                f"that does not"
                f"exist. First create the department.")

        new_user = User(username, email, department_id)
        self.users.append(new_user)

    def remove_user(self, _id: int):
        for index, user in enumerate(self.users):
            if user.id == _id:
                self.users.pop(index)
                return

        raise Exception(f"User with id of {_id} does not exist")

    def update_user(self, _id: int, updated_name: str):
        for user in self.users:
            if user.id == _id:
                user.username = updated_name
                return

        raise Exception(f"User with id of {_id} does not exist")

    def change_department(self, _id: int, new_department_id: int):
        if not self.department_exist(new_department_id):
            raise Exception(
                f"Department with ${id} does not exist. You cannot associate a user with a department that does not "
                f"exist. First create the department.")

        for user in self.users:
            if user.id == _id:
                user.departmentId = new_department_id
                return

        raise Exception(f"User with id of {_id} does not exist")

    def department_exist(self, department_id) -> bool:
        try:
            self.department_dao.get_single_department(department_id)
            return True
        except Exception:
            return False
