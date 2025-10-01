
from abc import ABC
class user(ABC):
    def __init__(self,name,phone,email,address):
        self.name=name
        self.phone=phone
        self.email=email
        self.address=address

class customer(user):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart=order()
    def view_menu(self,resturant):
        resturant.menu.show_menu()

    def add_to_cart(self,restaurant,item_name,quantity):
        item=restaurant.menu.find_item(item_name)
        if item :
            item.quantity=quantity
            self.cart.add_item(item)
            print("item added to cart")
        else:
            print("Item not found ")
    
    def view_cart(self):
        print("++++++cart++++++++")
        print("item_name\tprice\tquantity")
        for item ,quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
    print("Total Price:{self.cart.total_price}")

class order:
    def __init__(self):
        self.items={}
    
    def add_item(self,item):
        if item in self.items:
            self.items[item]+=item.quantity
        else:
            self.items[item]=item.quantity

    def remove(self,item):
        if item in self.items:
            del self.items[item]

    def total_price(self):
        return sum(item.price * quantity for item,quantity in self.items.items())
    
    def clear(self):
        self.items={}

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
     
    def add_employee(self,restaurant,employee):
        restaurant.add_employee(employee)

    def view_employee(self,restaurant):
        restaurant.view_employee()
    def add_new_item(self,resturant,item):
        resturant.menu.add_item(item)

    def delete_item(self,resturant,item):
        resturant.menu.remove_item(item)
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

class Menu:
    def __init__(self):
        self.items=[] #items database
        
    
    def add_item(self,item):
        self.items.append(item)
    def find_item(self,item_name):
        for item in self.items:
            if item.name.lower()== item_name.lower():
                return item 
            return None
    
    def remove_item(self,item_name):
        item=self.find_item(item_name)
        if item:
            self.items.remove(item)
            print("Item deleted successfully")
        else:
            print("Item not found ")        
    def show_menu(self):
        print("+++++++menu+++++++")
        print("Name\tprice\tQuantity")
        for item in self.items:
            print(f"{item.name}\t{item.price}\t{item.quantity}")

class FoodItem:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

        
    

#ad.add_employee("sagor","343123","sa@gmail.com","rajshai",32,"doc",1222233)
#ad.view_employee()
mama_res=Restaurant("Mamar resturant")
mn=Menu()

item=FoodItem("pizza",1200,10)
item1=FoodItem("burger",300,8)
item3=FoodItem("coffie",9,10)
ad=Admin("karim","121212","karim@gmail.com","dhaka")
ad.add_new_item(mama_res,item)
ad.add_new_item(mama_res,item1)
ad.add_new_item(mama_res,item3)

#creating customer

customer1=customer("fagun",171233,"fagun12@gmail.com","dhaka")
customer1.view_menu(mama_res)
