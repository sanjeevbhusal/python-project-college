from dao.User import UserDAO
from dao.Department import DepartmentDAO

department_dao = DepartmentDAO()
user_dao = UserDAO(department_dao)

print("Welcome to Employee Management System. Here is a quick introduction about the system and its working.")

print(
    '''This system will allow you to manage employees and departments in your company. You can perform CRUD operations (Create, Read, Update, Delete) on employees and departments. You can perform commands using numbers and alphabets that are pre-configured in the system. The system will guide you step by step on how to perform a command.

For Example, You can press 1 to perform operations on Employee. Similarly, Pressing 2 will let you perform operations on Departments. Once you have pressed 1 or 2, you will press other numbers to perform "Create", "Read", "Delete" and "Update" Operation. After performing a operation, you will be given an option to either continue with the system or exit out of the system.''')

print("\nLets Get Started.\n")

continue_playing = True

while continue_playing:

    print('''
Do you want to perform operations on Employee or Department? 

- Press 1 for Employee 
- Press 2 for Department
''')

    value = input("Your response: ")

    if value not in ["1", "2"]:
        print(f"You entered '{value}'. This is a Invalid Value. Please enter either 1 for Employee or 2 for Department")

    if int(value) == 1:
        print('''
You pressed 1. Now, you can perform operations on Employee. Here are all the operations available.

1. Create a new employee
2. Get all employees
3. Get single employee
4. Update employee name
5. Update employee department
6. Delete a employee 

Please press key associated with the command. Example: Press 1 for creating a new employee
''')

        command = input("Your Input: ")

        if command not in ["1", "2", "3", "4", "5", "6"]:
            print(f"You entered '{command}'. This is a Invalid Value. Please enter a valid input")

        command = int(command)

        if command == 1:
            print('''
You pressed '1'. Now, you can create a new User. Inorder to create a employee, you need to supply 3 things.

1. Username
2. Email
3. Department Id (This is the id of department user should be associated with).

Please note, If you donot have Department Id to associate the user, please create a department first.    
''')
            username = input("Enter the username: ")
            email = input("Enter the email: ")
            department_id = input("Enter the department id: ")

            try:
                user_dao.add_user(username, email, int(department_id))
                user_details = user_dao.get_all_users()[-1]
                print(f'''
The user has been added successfully. Here is the details of the user. 

{user_details}
                ''')
            except Exception as e:
                print(e)
        elif command == 2:
            users = user_dao.get_all_users()
            print(f'''
You pressed '2'. Here are all the employees 

{users}
 ''')
        elif command == 3:
            print('''
You pressed '3'. Inorder to get details about a user, you need to supply the following.

1. User Id 
''')
            user_id = input("Enter user Id: ")
            try:
                user = user_dao.get_single_user(int(user_id))
                print(f'''
Here is the details of the user. 

{user}
 ''')
            except Exception as e:
                print(e)
        elif command == 4:
            print('''
You pressed '4'. Inorder to update a employee name, you need to supply the following.

1. New Name
2. User Id
''')
            user_id = input("Enter user Id: ")
            new_name = input("Enter new Name: ")
            try:
                user = user_dao.update_user(int(user_id), new_name)
                print(f'''User's name has been successfully updated.''')
            except Exception as e:
                print(e)
        elif command == 5:
            print('''
You pressed '5'. Inorder to update a employee's department, you need to supply the following.

1. New Department ID
''')
            user_id = input("Enter user Id: ")
            department_id = input("Enter new Department Id: ")
            try:
                user = user_dao.change_department(int(user_id), int(department_id))
                print(f'''User's department has been successfully updated.''')
            except Exception as e:
                print(e)
        else:
            print('''
You pressed '6'. Inorder to delete a employee, you need to supply the following.

1. Employee ID
''')
            user_id = input("Enter user Id: ")
            try:
                user = user_dao.remove_user(int(user_id))
                print(f'''User has been successfully deleted.''')
            except Exception as e:
                print(e)
    else:
        print('''
You pressed 2. Now, you can perform operations on Department. Here are all the operations available.

1. Create a new department
2. Get all departments
3. Get single department
4. Update department name
5. Delete a department 

Please press key associated with the command. Example: Press 1 for creating a new department
''')

        command = input("Your Input: ")

        if command not in ["1", "2", "3", "4", "5", "6"]:
            print(f"\nYou entered '{command}'. This is a Invalid Value. Please enter a valid input")
            continue

        command = int(command)

        if command == 1:
            print('''
You pressed '1'. Now, you can create a new Department. Inorder to create a department, you need to supply the following values.

1. Name of the department
        ''')

            name = input("Enter the department name: ")

            try:
                department_dao.add_department(name)
                department_details = department_dao.get_all_departments()[-1]
                print(f'''
The department has been added successfully. Here is the details of the department. 

{department_details}
''')
            except Exception as e:
                pass
        elif command == 2:
            departments = department_dao.get_all_departments()
            print(f'''
You pressed '2'. Here are all the departments 

{departments}
 ''')
        elif command == 3:
            print('''
You pressed '3'. Inorder to get details about a department, you need to supply the following.

1. Department Id 
''')
            department_id = input("Enter department Id: ")
            try:
                department = department_dao.get_single_department(int(department_id))
                print(f'''
Here is the details of the department. 

{department}
 ''')
            except Exception as e:
                print(e)
        elif command == 4:
            print('''
You pressed '4'. Inorder to update a department name, you need to supply the following.

1. New Name
2. Department Id
''')
            department_id = input("Enter department Id: ")
            new_name = input("Enter new Name: ")
            try:
                user = department_dao.update_department(int(department_id), new_name)
                print(f'''Department's name has been successfully updated.''')
            except Exception as e:
                print(e)
        else:
            print('''
You pressed '5'. Inorder to delete a department, you need to supply the following.

1. Department ID
''')
            department_id = input("Enter department Id: ")
            try:
                department = department_dao.remove_department(int(department_id))
                print(f'''\nDepartment has been successfully deleted.''')
            except Exception as e:
                print(e)

    print('''
DO you want to continue working on the system. 
1. Press 'N' for No
2. Press 'Any Other Key' for Yes
''')

    response = input("Your response: ").lower()
    if response == "n":
        continue_playing = False
