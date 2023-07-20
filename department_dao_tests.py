import unittest
from dao.Department import DepartmentDAO  # Replace "your_module" with the actual module name
from models.Department import Department


class TestDepartmentDAO(unittest.TestCase):
    def setUp(self):
        # Create a test instance of DepartmentDAO for each test case
        self.department_dao = DepartmentDAO()

    def test_add_department(self):
        initial_count = len(self.department_dao.get_all_departments())

        # Add a new department
        self.department_dao.add_department("HR")

        # Assert that the department was added
        self.assertEqual(len(self.department_dao.get_all_departments()), initial_count + 1)

    def test_remove_department(self):
        # Add a department first
        self.department_dao.add_department("Marketing")

        # Get the department ID of the newly added department
        department_id = self.department_dao.get_all_departments()[-1].id

        # Remove the department
        self.department_dao.remove_department(department_id)

        # Assert that the department was removed
        self.assertNotIn(department_id, [department.id for department in self.department_dao.get_all_departments()])

    def test_get_single_department(self):
        # Add a department first
        self.department_dao.add_department("Finance")

        # Get the department ID of the newly added department
        department_id = self.department_dao.get_all_departments()[-1].id

        # Get the department by ID using the method
        department = self.department_dao.get_single_department(department_id)

        # Assert that the retrieved department is the same as the one we added
        self.assertEqual(department.id, department_id)
        self.assertEqual(department.name, "Finance")

    def test_get_single_department_nonexistent(self):
        # Try to get a department with a non-existent ID
        non_existent_id = 99999

        # Assert that an exception is raised
        with self.assertRaises(Exception):
            self.department_dao.get_single_department(non_existent_id)

    def test_update_department(self):
        # Add a department first
        self.department_dao.add_department("IT")

        # Get the department ID of the newly added department
        department_id = self.department_dao.get_all_departments()[-1].id

        # Update the department name
        updated_name = "Information Technology"
        self.department_dao.update_department(department_id, updated_name)

        # Get the department by ID and assert the name is updated
        department = self.department_dao.get_single_department(department_id)
        self.assertEqual(department.name, updated_name)


if __name__ == '__main__':
    unittest.main()
