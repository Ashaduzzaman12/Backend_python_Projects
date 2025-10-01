
from abc import ABC
class user(ABC):
    def __init__(self,name,phone,email,address):
        self.name=name
        self.phone=phone
        self.email=email
        self.address=address


class Employee(user):
    def __init__(self, name, phone, email, address,age,designation,salary):
        super().__init__(name, phone, email, address)
        self.age=age
        self.designation=designation
        self.salary=salary

#emp=Employee("rahim",4474142,"rahim01@gmail.com","dhaka",32,"chef",30000)
#print(emp.age)

class Admin(user):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.employees=[] #database
    
    def add_employee(self,name,phone,email,address,age,designation,salary):
        employee=Employee(name,phone,email,address,age,designation,salary)
        self.employees.append(employee)
        print(f"{employee.name} is added ")

    def view_employee(self):
        print("Employee list ::")
        for emp in self.employees:
            print(emp.name,emp.email,emp.address)

ad=Admin("karim","121212","karim@gmail.com","dhaka")
ad.add_employee("sagor","343123","sa@gmail.com","rajshai",32,"doc",1222233)
ad.view_employee()