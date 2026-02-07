import random
import os
import json


class Employee:

    # Creating a constructor with an empty dictionary when the user instantiate an Employee
    def __init__(self):
        self.employees = {}

    # Method that populates employee dictionary
    def add_employee(self, employee_name, employee_age, employee_position, employee_salary, employee_location,
                     employee_department):

        employee_id = random.randint(1, 100)

        employee_data = {
            "__id": employee_id,
            "__name": employee_name,
            "__age": employee_age,
            "__position": employee_position,
            "__salary": employee_salary,
            "location": employee_location,
            "department": employee_department,
        }

        self.write_employee(employee_data)

    def write_employee(self, employee: dict):
        flags = os.O_WRONLY | os.O_CREAT | os.O_TRUNC
        employee_file_json = ""

        if not "Current_Employees.json":
            employee_file_json = os.open("Current_Employees.json", flags, 0o644)

        if employee.id in self.employees:
            print("Employee already exist")
        else:
            json_string = json.dumps(employee, indent=4)
            os.write(employee_file_json, json_string.encode("utf-8"))
            os.close(employee_file_json)

    # Method that display employees
    def display_employees(self):
        with open("Current_Employees.json", "r") as file:
            content = file.read()
            print(content)
