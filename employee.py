import random
import os
import json

from main import newEmployee, new_employee_name


class Employee:

    # Creating a constructor with an empty dictionary when the user instantiate an Employee
    def __init__(self, name, age, position, salary, location, department):

        self.__employee_name = name
        self.__employee_age = age
        self.__employee_position = position
        self.__employee_salary = salary
        self.employee_location = location
        self.employee_department = department

    #Get Method to transform the employee into a dictionary
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


    #Get Method to get employee name
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

    #Method to crearte and save the employee into a file

    def save_employee(self):
        output_file = "Current_Employees.json"
        employee_data = []

        try:
            with open(output_file, "r") as file:
                #If there is any file in json, it will convert into python language
                employee_data = json.load(file)
        except (FileNotFoundError,json.JSONDecodeError):
            employee_data = []

        for employee in employee_data:
            if employee["name"] == self.__employee_name and employee["position"] == self.__employee_position:
                print(f"The {employee["name"]} already exists")
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
                        print(f"ID: {employee["id"]} - Name: {employee['name']} - Age: {employee['age']} - Position: {employee['position']} - Salary: {employee['salary']} - Location: {employee['location']} - Department: {employee['department']}")
        except FileNotFoundError:
            print("\nNo employee file found. Please add an employee first.\n")


    def update_employee(self, employee_id, update_data: dict):

        new_employee = []
        try:
            with open("Current_Employees.json", "r") as file:
                content = json.load(file)

                if not content:
                    print("Employees are empty")
                    return
        except FileNotFoundError:
            print("Employee file not found. Please add an employee first.\n")

        try:
            with open("Current_Employees.json", "r") as file:
                content = json.load(file)

                # TODO: Check how to populate the new opject to save it into the file

                if employee_id == content["id"]:
                    current_employee = self.get_employee_object()
                    new_employee.append(current_employee)

                    for employee in content:
                        if update_data["name"] != "":
                            employee.get_employee_name(update_data["name"])
                        if update_data["age"] != "":
                            employee.get_employee_age(update_data["age"])
                        if update_data["salary"] != "":
                            employee.get_employee_salary(update_data["salary"])
                        if update_data["position"] != "":
                            employee.get_employee_position(update_data["position"])
                        if update_data["department"] != "":
                            employee["department"] = update_data["department"]
                        if update_data["location"] != "":
                            employee["location"] = update_data["location"]
                print("Employee updated successfully")


        except FileNotFoundError:
            print("Employee file not found. Please add an employee first.\n")

