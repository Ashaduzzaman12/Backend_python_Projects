class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.balance = 0
        self.orders = []

    def view_menu(self, menu):
        print("---- MENU ----")
        for item, price in menu.items():
            print(f"{item}: ৳{price}")

    def place_order(self, restaurant, item):
        if item not in restaurant.menu:
            print(f"Sorry, {item} is not available.")
            return
        price = restaurant.menu[item]
        if self.balance >= price:
            self.balance -= price
            self.orders.append(item)
            print(f"Order placed: {item} for ৳{price}")
        else:
            print("Insufficient balance.")

    def check_balance(self):
        print(f"Available Balance: ৳{self.balance}")

    def view_orders(self):
        print("Placed Orders:")
        if not self.orders:
            print("No orders yet.")
        else:
            for order in self.orders:
                print(f"- {order}")

    def add_funds(self, amount):
        self.balance += amount
        print(f"৳{amount} added to balance. New balance is ৳{self.balance}")


class Admin:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def add_menu_item(self, restaurant, item, price):
        restaurant.menu[item] = price
        print(f"Item '{item}' added with price ৳{price}.")

    def remove_menu_item(self, restaurant, item):
        if item in restaurant.menu:
            del restaurant.menu[item]
            print(f"Item '{item}' removed from menu.")
        else:
            print("Item not found in menu.")

    def update_menu_price(self, restaurant, item, new_price):
        if item in restaurant.menu:
            restaurant.menu[item] = new_price
            print(f"Updated price of '{item}' to ৳{new_price}.")
        else:
            print("Item not found in menu.")

    def add_customer(self, restaurant, name, email, address):
        if email in restaurant.customers:
            print("Customer already exists.")
        else:
            restaurant.customers[email] = Customer(name, email, address)
            print(f"Customer '{name}' added.")

    def remove_customer(self, restaurant, email):
        if email in restaurant.customers:
            del restaurant.customers[email]
            print(f"Customer with email '{email}' removed.")
        else:
            print("Customer not found.")

    def view_customers(self, restaurant):
        print("Registered Customers:")
        for cust in restaurant.customers.values():
            print(f"- {cust.name}, Email: {cust.email}, Address: {cust.address}, Balance: ৳{cust.balance}")


class Restaurant:
    def __init__(self):
        self.menu = {}
        self.customers = {}

    def show_menu(self):
        print("Restaurant Menu:")
        for item, price in self.menu.items():
            print(f"{item}: ৳{price}")

    def get_customer(self, email):
        return self.customers.get(email)

    def add_customer(self, customer):
        if customer.email not in self.customers:
            self.customers[customer.email] = customer
            print(f"Customer '{customer.name}' added to system.")
        else:
            print("Customer already exists.")

    def remove_customer(self, email):
        if email in self.customers:
            del self.customers[email]
            print(f"Customer with email '{email}' removed.")
        else:
            print("Customer not found.")




restaurant = Restaurant()
admin = Admin("Admin", "mushfiqurrahman.dm@gmail.com")

 
admin.add_menu_item(restaurant, "Burger", 60)
admin.add_menu_item(restaurant, "Pizza", 200)
admin.add_menu_item(restaurant, "Coffee", 50)


admin.add_customer(restaurant, "Tousif", "tousif@gmail.com", "Gulshan, Dhaka")


customer = restaurant.get_customer("tousif@gmail.com")
customer.add_funds(300)
customer.view_menu(restaurant.menu)
customer.place_order(restaurant, "Pizza")
customer.place_order(restaurant, "Coffee")
customer.check_balance()
customer.view_orders()


admin.view_customers(restaurant)
admin.update_menu_price(restaurant, "Pizza", 180)
restaurant.show_menu()

