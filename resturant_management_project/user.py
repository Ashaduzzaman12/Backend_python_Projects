
from abc import ABC
from orders import order
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
            if quantity >item.quantity:
                print("Item quantity exceeded")
            else:
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
        print(f"Total Price: {self.cart.total_price}")
    def pay_bill(self):
        print(f"Total{self.cart.total_price}paid successfully")
        self.cart.clear()


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
    def view_menu(self,restaurent):
        restaurent.manu.show_menu()



