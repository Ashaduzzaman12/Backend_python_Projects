from menu import Menu
from user import Employee
class Restaurant:
    def __init__(self,name):
        self.name=name
        self.employees=[] #database
        self.menu=Menu()
    def add_employee(self,employee):
        employee=Employee(employee)
        self.employees.append(employee)
        print(f"{employee.name} is added ")

    def view_employee(self):
        print("Employee list ::")
        for emp in self.employees:
            print(emp.name,emp.email,emp.address)
