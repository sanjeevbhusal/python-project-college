from typing import List

from models.Department import Department


class DepartmentDAO:
    def __init__(self):
        self.departments: List[Department] = []

    def get_all_departments(self):
        return self.departments

    def get_single_department(self, _id: int):
        for department in self.departments:
            if department.id == _id:
                return department

        raise Exception(f"Department with {_id} does not exist")

    def add_department(self, name: str):
        new_department = Department(name)
        self.departments.append(new_department)

    def remove_department(self, _id: int):
        for index, department in enumerate(self.departments):
            if department.id == _id:
                self.departments.pop(index)
                return

        raise Exception(f"Department with {_id} does not exist")

    def update_department(self, _id: int, updated_name: str):
        for department in self.departments:
            if department.id == _id:
                department.name = updated_name
                return

        raise Exception(f"Department with {_id} does not exist")
