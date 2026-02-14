import employee
from employee import Employee

# While loop that will be running until the user hits option 5.
while True:
    print("*****************************************")
    print("\n ***** Welcome to Employee Manager System: ****** \n")
    print("***************************************** \n")
    print("1. Add a new employee in the system")
    print("2. Display all employees")
    print("3. Update any employee information")
    print("4. Delete employee")
    print("5. Search Employee")
    print("6. Sort the employees list")
    print("7. Exit \n")

    # I am using a Try Exception in order to catch user input error and avoid my program breaks
    try:
        option = int(input("What would you like to do?: "))

        # Condition validation that will lead the user through the options available
        if option == 1:
            print("Ok...Let's add a new employee in the system")
            name = input("What is the employee name? ")
            age = input("What is the employee age? ")
            position = input("What is the employee position? ")
            salary = input("What is the employee salary? ")
            location = input("Where is the employee based? ")
            department = input("What is the employee department?")

            newEmployee = employee.Employee(name, age, position, salary, location, department)
            newEmployee.save_employee()

        elif option == 2:
            back = True

            while back:
                # Function that display all employees
                employee.Employee.display_employees()

                userAnswer = input("Press R to return to the main menu...")

                if userAnswer:
                    back = False

        elif option == 3:

            back = True

            # Transforming ID into a number since my JSON receives a number
            try:
                employee_id = int(input("What is the employee id? "))
            except ValueError:
                print("ID must be a number")

            field_to_update = input("What information do you want to update?").lower()

            value_to_update = ""

            match field_to_update:
                case "name":
                    value_to_update = input("Enter the new name? ")
                case "age":
                    value_to_update = input("Enter the new age")
                case "position":
                    value_to_update = input("Enter the new position")
                case "salary":
                    value_to_update = input("Enter the new salary")
                case "location":
                    value_to_update = input("Enter the new location")
                case "department":
                    value_to_update = input("Enter the new department")
                case _:
                    print("Please enter with an option available in the menu.")
                    continue

            while back:
                Employee.update_employee(employee_id, field_to_update, value_to_update)

                userAnswer = input("Press R to return to the main menu...")

                if userAnswer:
                    back = False

        elif option == 4:
            back = True

            # Transforming ID into a number since my JSON receives a number
            try:
                employee_id = int(input("What is the employee id to be deleted? "))
                employee_name = input("What is the employee name to be deleted? ")

            except ValueError:
                print("ID must be a number")

            while back:
                Employee.delete_employee(employee_id, employee_name)

                userAnswer = input("Press R to return to the main menu...")

                if userAnswer:
                    back = False

        elif option == 5:

            back = True

            employee_name = input("What is the employee name you want to find? ")

            while back:
                Employee.search_employee(employee_name)

                userAnswer = input("Press R to return to the main menu...")

                if userAnswer:
                    back = False

        elif option == 6:
            back = True
            print("Type salary, if you would like to sort the employee list by salary")
            print("Type position, if you would like to sort the employee list by position\n")
            user_input = input("")

            while back:
                Employee.sort_employee_list(user_input)

                userAnswer = input("Press R to return to the main menu...")

                if userAnswer:
                    back = False

        elif option == 7:
            break

    except ValueError:
        print("Please enter with an option available in the menu.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
