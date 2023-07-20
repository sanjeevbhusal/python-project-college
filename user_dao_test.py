import unittest
from dao.User import UserDAO  # Replace "your_module" with the actual module name
from models.User import User
from dao.Department import DepartmentDAO  # Replace "your_module" with the actual module name
from models.Department import Department


class TestUserDAO(unittest.TestCase):
    def setUp(self):
        # Create a test instance of DepartmentDAO for each test case
        self.department_dao = DepartmentDAO()

        # Create a test instance of UserDAO for each test case
        self.user_dao = UserDAO(self.department_dao)

    def test_add_user_to_existing_department(self):
        # Add a department first
        self.department_dao.add_department("HR")

        # Get the department ID of the newly added department
        department_id = self.department_dao.get_all_departments()[-1].id

        initial_count = len(self.user_dao.get_all_users())

        # Add a new user to the existing department
        self.user_dao.add_user("John Doe", "john@example.com", department_id)

        # Assert that the user was added
        self.assertEqual(len(self.user_dao.get_all_users()), initial_count + 1)

    def test_add_user_to_nonexistent_department(self):
        non_existent_department_id = 99999

        # Assert that an exception is raised when adding a user to a nonexistent department
        with self.assertRaises(Exception):
            self.user_dao.add_user("Jane Smith", "jane@example.com", non_existent_department_id)

    def test_get_single_user(self):
        # Add a department and user
        self.department_dao.add_department("IT")
        department_id = self.department_dao.get_all_departments()[-1].id
        self.user_dao.add_user("Alice", "alice@example.com", department_id)

        # Get the user ID of the newly added user
        user_id = self.user_dao.get_all_users()[-1].id

        # Get the user by ID using the method
        user = self.user_dao.get_single_user(user_id)

        # Assert that the retrieved user is the same as the one we added
        self.assertEqual(user.id, user_id)
        self.assertEqual(user.username, "Alice")

    def test_get_single_user_nonexistent(self):
        # Try to get a user with a non-existent ID
        non_existent_id = 99999

        # Assert that an exception is raised
        with self.assertRaises(Exception):
            self.user_dao.get_single_user(non_existent_id)

    def test_remove_user(self):
        # Add a department and user
        self.department_dao.add_department("Finance")
        department_id = self.department_dao.get_all_departments()[-1].id
        self.user_dao.add_user("Bob", "bob@example.com", department_id)

        # Get the user ID of the newly added user
        user_id = self.user_dao.get_all_users()[-1].id

        # Remove the user
        self.user_dao.remove_user(user_id)

        # Assert that the user was removed
        self.assertNotIn(user_id, [user.id for user in self.user_dao.get_all_users()])

    def test_update_user(self):
        self.department_dao.add_department("HR")
        department_id = self.department_dao.get_all_departments()[-1].id
        self.user_dao.add_user("Charlie", "charlie@example.com", department_id)

        # Get the user ID of the newly added user
        user_id = self.user_dao.get_all_users()[-1].id

        # Update the user name
        updated_name = "Charlie Brown"
        self.user_dao.update_user(user_id, updated_name)

        # Get the user by ID and assert the name is updated
        user = self.user_dao.get_single_user(user_id)
        self.assertEqual(user.username, updated_name)

    def test_change_user_department(self):
        # Add 2 departments first
        self.department_dao.add_department("IT")
        self.department_dao.add_department("Finance")

        # Get the department IDs
        department_id_it = self.department_dao.get_all_departments()[-2].id
        department_id_finance = self.department_dao.get_all_departments()[-1].id

        # Add a user in IT department
        self.user_dao.add_user("Charlie", "charlie@example.com", department_id_it)
        user_id = self.user_dao.get_all_users()[-1].id

        # Change the user's department to "Finance"
        self.user_dao.change_department(user_id, department_id_finance)

        # Get the user by ID and assert the departmentId is updated
        user = self.user_dao.get_single_user(user_id)
        self.assertEqual(user.departmentId, department_id_finance)

        # Change the user's department back to "IT"
        self.user_dao.change_department(user_id, department_id_it)

        # Get the user by ID and assert the departmentId is updated
        user = self.user_dao.get_single_user(user_id)
        self.assertEqual(user.departmentId, department_id_it)


if __name__ == '__main__':
    unittest.main()
