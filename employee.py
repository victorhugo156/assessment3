import random
import json


class Employee:

    # Creating a constructor with an empty dictionary when the user instantiate an Employee
    def __init__(self, name, age, position, salary, location, department):

        self.__employee_name = name
        self.__employee_age = age
        self.__employee_position = position
        self.__employee_salary = salary
        self.employee_location = location
        self.employee_department = department

    # Get Method to transform the employee into a dictionary
    def get_employee_object(self):
        employee_id = random.randint(1, 100)
        return {
            "id": employee_id,
            "name": self.__employee_name,
            "age": self.__employee_age,
            "position": self.__employee_position,
            "salary": self.__employee_salary,
            "location": self.employee_location,
            "department": self.employee_department,
        }

    # Get Method to get employee name
    def get_employee_name(self):
        return self.__employee_name

    # Get Method to get employee age
    def get_employee_age(self):
        return self.__employee_age

    # Get Method to get employee position
    def get_employee_position(self):
        return self.__employee_position

    # Get Method to get employee position
    def get_employee_salary(self):
        return self.__employee_salary

    # Method to crearte and save the employee into a file

    def save_employee(self):
        output_file = "Current_Employees.json"
        employee_data = []

        try:
            with open(output_file, "r") as file:
                # If there is any file in json, it will convert into python language
                employee_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            employee_data = []

        for employee in employee_data:
            if employee["name"] == self.__employee_name and employee["position"] == self.__employee_position:
                print(f"The {employee['name']} already exists")
                return

        current_employee = self.get_employee_object()
        employee_data.append(current_employee)

        try:
            with open(output_file, "w") as file:
                json.dump(employee_data, file, indent=4)
                print(f"Employee {self.__employee_name} has been saved into the file:  {output_file}")
        except Exception as e:
            print(f"Error while saving employee data: {e}")

    # Method that display employees
    @staticmethod
    def display_employees():
        try:
            with open("Current_Employees.json", "r") as file:
                content = json.load(file)

                if not content:
                    print("Employees are empty")
                else:
                    print("\n--- List of Employees ---")
                    for employee in content:
                        print(
                            f"ID: {employee['id']} - Name: {employee['name']} - Age: {employee['age']} - Position: {employee['position']} - Salary: {employee['salary']} - Location: {employee['location']} - Department: {employee['department']}")
        except FileNotFoundError:
            print("\nNo employee file found. Please add an employee first.\n")

    @staticmethod
    def update_employee(employee_id, field_to_update, value_to_update):
        file_name = "Current_Employees.json"

        # Reading the file
        try:
            with open(file_name, "r") as file:
                employees_list = json.load(file)

                if not employees_list:
                    print("Employees are empty")
                    return
        except (FileNotFoundError, json.JSONDecodeError):
            print("No employees found to be updated\n")
            return

        employee_found = False
        for employee in employees_list:

            if employee["id"] == employee_id:
                if field_to_update == "name":
                    employee["name"] = value_to_update

                elif field_to_update == "age":
                    employee["age"] = value_to_update
                elif field_to_update == "position":
                    employee["position"] = value_to_update
                elif field_to_update == "salary":
                    employee["salary"] = value_to_update
                elif field_to_update == "location":
                    employee["location"] = value_to_update
                elif field_to_update == "department":
                    employee["department"] = value_to_update

                print(f"Updated {value_to_update} for ID {employee_id}.")
                employee_found = True
                break

        if not employee_found:
            print(f"Employee with ID {employee_id} not found.")
            return

        # Saving employee into the file
        try:
            with open(file_name, "w") as file:
                json.dump(employees_list, file, indent=4)

            print("Employee updated successfully")
        except Exception as e:
            print(f"Error saving file: {e}")

    @staticmethod
    def delete_employee(employee_id, employee_name):
        file_name = "Current_Employees.json"

        # Reading the file
        try:
            with open(file_name, "r") as file:
                employees_list = json.load(file)

                if not employees_list:
                    print("Employees are empty")
                    return
        except (FileNotFoundError, json.JSONDecodeError):
            print("No employees found to be updated\n")
            return

        employee_found = False

        for employee in employees_list:

            if employee["id"] == employee_id:

                user_confirmation = input(f"Type YES if you want to delete the employee\n{employee}\n or type NO if "
                                          f"you want to return").lower()
                if user_confirmation == "yes":
                    employees_list.remove(employee)
                    print(f"Employee: {employee_name} has been deleted")
                    employee_found = True
                    break
                else:
                    return

        if not employee_found:
            print(f"Employee with ID {employee_id} not found.")
            return

        try:
            with open(file_name, "w") as file:
                json.dump(employees_list, file, indent=4)
            print("Data Base has been updated successfully.")
        except Exception as e:
            print(f"Error saving file: {e}")

    @staticmethod
    def search_employee(employee_name):
        file_name = "Current_Employees.json"

        # Reading the file
        try:
            with open(file_name, "r") as file:
                employees_list = json.load(file)

                if not employees_list:
                    print("Employees are empty")
                    return
        except (FileNotFoundError, json.JSONDecodeError):
            print("No employees found to be updated\n")
            return

        employee_found = False

        for employee in employees_list:

            if employee["name"] == employee_name:
                print(f"Employee: {employee} has been deleted")
                employee_found = True

        if not employee_found:
            print(f"Employee: {employee_name} not found.")
            return
