from dao.User import UserDAO
from dao.Department import DepartmentDAO

department_dao = DepartmentDAO()
user_dao = UserDAO(department_dao)

print("                                           Welcome to Employee Management System.                  \n")

print(
    "This system will allow you to manage employees and departments in your company. You can perform CRUD operations"
    "(Create, Read, Update, Delete) on any employee and department. You can perform commands using numbers and "
    "alphabets that are pre-configured.\n")

print(
    "For Example, You can press 1 to perform operations on Employee. Similarly, Pressing 2 will let you perform "
    "operations on Departments. Once you have pressed 1 or 2, you can then further press alphabets such as 'C' ("
    "(Create), 'D' (Delete) and 'U' (Update) \n")

print("                                                       Lets get Started.                  \n")

while True:
    value = input(
        "Do you want to perform operations on Employee or Department? Press 1 for Employee or Press 2 for Department:   ", )

    print("")

    if value not in ["1", "2"]:
        print(f"You entered '{value}'. This is a Invalid Value. Please enter either 1 for Employee or 2 for Department")

    if int(value) == 1:
        print("You pressed 1. Now, you can perform operations on Employee.\n")
    elif int(value) == 2:
        print("You pressed 2. Now, you can perform operations on Department")

    print(
        "You can either create a new employee, update the name and department id of existing employee or delete a "
        "employee. Please press keyword associated with the command. You can type the command in both small case or "
        "upper"
        "case\n")

    print("Press 'C' to Create a New User\nPress 'U' to Update a existing User\nPress 'D' to Delete a user\n")

    command = input("Your Input: ")

    print()

    if command.lower() not in ["c", "u", "d"]:
        print(f"You entered '{command}'. This is a Invalid Value. Please enter either 'C' for creating a new user, "
              f"'U' for updating a user or 'D' for deleting a user")

    command = command.lower()

    if command == "c":
        print("You pressed 'C'. Now, you can create a new User\n")
        print(
            "Inorder to create a user, you need to supply a username, email and department ID of the department user is"
            "associated with. Please note, if the department is not yet created, a User cannot be created.\n")

        username = input("Enter the username: ")
        email = input("Enter the email: ")
        department_id = input("Enter the department id:  ")

        try:
            user_dao.add_user(username, email, department_id)
        except Exception as e:
            print()
            print(e)
            print("\nLets start from Beginning.\n")
