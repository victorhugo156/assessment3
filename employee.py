import random


class Employee:

    # Creating a constructor with an empty dictionary when the user instantiate an Employee
    def __init__(self):
        self.employees = {}

    # Method that populates employee dictionary
    def add_employee(self, employee_name, employee_age, employee_position, employee_salary, employee_location, employee_department):
        employee_id = random.randint(1, 100)
        self.employees[employee_id] = {
            "__name": employee_name,
            "__age": employee_age,
            "__position": employee_position,
            "__salary": employee_salary,
            "location": employee_location,
            "department": employee_department,
        }

    # Method that display employees
    def display_employee(self):
        for employee in self.employees.items():
            print(employee)
